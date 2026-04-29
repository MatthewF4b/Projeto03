import csv
from jogo import Jogo
from filabacklog import FilaBacklog
from pilharecentes import PilhaRecentes
from sessao import SessaoJogo


def to_float(valor):
    try:
        return float(valor)
    except:
        return 0.0


class SteamPy:
    def __init__(self):
        self.catalogo = []
        self.backlog = FilaBacklog()
        self.recentes = PilhaRecentes()
        self.historico = []
        self.tempos = {}

    def carregar_jogos(self, arquivo):
        with open(arquivo, encoding="utf-8") as f:
            leitor = csv.reader(f)
            next(leitor)

            for i, linha in enumerate(leitor):
                try:
                    jogo = Jogo(
                        i,
                        linha[1],
                        linha[2],
                        linha[3],
                        linha[4],
                        linha[5],
                        to_float(linha[6]),
                        to_float(linha[7]),
                        to_float(linha[8]),
                        to_float(linha[9]),
                        to_float(linha[10]),
                        to_float(linha[11]),
                        linha[12]
                    )
                    self.catalogo.append(jogo)
                except:
                    continue

        print("Catálogo carregado!")

    def listar(self):
        for jogo in self.catalogo[:20]:
            print(jogo.exibir())

    def buscar(self, nome):
        for jogo in self.catalogo:
            if nome.lower() in jogo.titulo.lower():
                print(jogo.exibir())

    def adicionar_backlog(self, id_jogo):
        if id_jogo < len(self.catalogo):
            jogo = self.catalogo[id_jogo]
            self.backlog.enqueue(jogo)
            print("Adicionado ao backlog!")
        else:
            print("ID inválido")

    def jogar_proximo(self):
        jogo = self.backlog.dequeue()
        if jogo:
            print("Jogando:", jogo.titulo)
            self.recentes.push(jogo)
            return jogo
        else:
            print("Backlog vazio")
            return None

    def registrar_tempo(self, jogo, tempo):
        total = self.tempos.get(jogo.id, 0) + tempo
        self.tempos[jogo.id] = total

        sessao = SessaoJogo(jogo, tempo, total)
        self.historico.append(sessao)

        with open("historico_jogo.txt", "a", encoding="utf-8") as f:
            f.write(sessao.linha() + "\n")

        print("Sessão registrada!")

    def dashboard(self):
        total_tempo = sum(self.tempos.values())

        print("\n--- DASHBOARD ---")
        print("Total jogos no catálogo:", len(self.catalogo))
        print("Jogos no backlog:", self.backlog.tamanho())
        print("Jogos recentes:", self.recentes.tamanho())
        print("Sessões jogadas:", len(self.historico))
        print("Tempo total jogado:", total_tempo)

    def recomendar(self):
        print("\n--- RECOMENDAÇÃO ---")

        generos = {}
        for s in self.historico:
            g = s.jogo.genero
            generos[g] = generos.get(g, 0) + 1

        if not generos:
            print("Sem dados ainda")
            return

        favorito = max(generos, key=generos.get)

        for jogo in self.catalogo:
            if jogo.genero == favorito and jogo.id not in self.tempos:
                print("Baseado no seu gênero favorito:", favorito)
                print(jogo.exibir())
                break