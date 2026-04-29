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

    # ---------------------------
    # CARREGAR
    # ---------------------------
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

    # ---------------------------
    # LISTAR / BUSCAR
    # ---------------------------
    def listar(self):
        for jogo in self.catalogo[:50]:
            print(jogo.exibir())

    def buscar(self, nome):
        for jogo in self.catalogo:
            if nome.lower() in jogo.titulo.lower():
                print(jogo.exibir())

    # ---------------------------
    # FILTROS
    # ---------------------------
    def filtrar_genero(self, genero):
        for jogo in self.catalogo:
            if jogo.genero.lower() == genero.lower():
                print(jogo.exibir())

    def filtrar_console(self, console):
        for jogo in self.catalogo:
            if jogo.console.lower() == console.lower():
                print(jogo.exibir())

    def filtrar_nota(self, nota):
        for jogo in self.catalogo:
            if jogo.critic_score >= nota:
                print(jogo.exibir())

    # ---------------------------
    # ORDENAÇÃO
    # ---------------------------
    def ordenar(self, criterio):
        if criterio == "titulo":
            lista = sorted(self.catalogo, key=lambda x: x.titulo)
        elif criterio == "nota":
            lista = sorted(self.catalogo, key=lambda x: x.critic_score, reverse=True)
        elif criterio == "vendas":
            lista = sorted(self.catalogo, key=lambda x: x.total_sales, reverse=True)
        else:
            print("Critério inválido")
            return

        for jogo in lista[:50]:
            print(jogo.exibir())

    # ---------------------------
    # BACKLOG
    # ---------------------------
    def adicionar_backlog(self, id_jogo):
        if id_jogo < len(self.catalogo):
            self.backlog.enqueue(self.catalogo[id_jogo])
            print("Adicionado!")
        else:
            print("ID inválido")

    def jogar_proximo(self):
        jogo = self.backlog.dequeue()
        if jogo:
            print("Jogando:", jogo.titulo)
            self.recentes.push(jogo)
            return jogo
        print("Backlog vazio")

    def salvar_backlog(self):
        with open("backlog.txt", "w", encoding="utf-8") as f:
            for jogo in self.backlog.dados:
                f.write(f"{jogo.id};{jogo.titulo};{jogo.console}\n")
        print("Backlog salvo!")

    # ---------------------------
    # RECENTES
    # ---------------------------
    def ver_recentes(self):
        self.recentes.mostrar()

    def retomar(self):
        jogo = self.recentes.topo()
        if jogo:
            print("Retomando:", jogo.titulo)
            self.recentes.push(jogo)
            return jogo
        print("Nenhum jogo recente")

    # ---------------------------
    # SESSÃO
    # ---------------------------
    def registrar_tempo(self, jogo, tempo):
        total = self.tempos.get(jogo.id, 0) + tempo
        self.tempos[jogo.id] = total

        sessao = SessaoJogo(jogo, tempo, total)
        self.historico.append(sessao)

        print("Sessão registrada!")

    def ver_historico(self):
        for s in self.historico:
            print(s.linha())

    # ---------------------------
    # RECOMENDAÇÃO
    # ---------------------------
    def recomendar(self):
        generos = {}

        for s in self.historico:
            g = s.jogo.genero
            generos[g] = generos.get(g, 0) + 1

        if not generos:
            print("Sem dados")
            return

        favorito = max(generos, key=generos.get)

        print("Baseado no gênero:", favorito)

        for jogo in self.catalogo:
            if jogo.genero == favorito and jogo.id not in self.tempos:
                print(jogo.exibir())
                break

    # ---------------------------
    # RANKING
    # ---------------------------
    def ranking(self):
        if not self.tempos:
            print("Sem dados")
            return

        ordenado = sorted(self.tempos.items(), key=lambda x: x[1], reverse=True)

        print("\n--- RANKING ---")
        for id_jogo, tempo in ordenado[:10]:
            print(self.catalogo[id_jogo].exibir(), "Horas:", tempo)

    # ---------------------------
    # DASHBOARD
    # ---------------------------
    def dashboard(self):
        print("\n--- DASHBOARD ---")
        print("Total jogos:", len(self.catalogo))
        print("Backlog:", self.backlog.tamanho())
        print("Recentes:", self.recentes.tamanho())
        print("Sessões:", len(self.historico))
        print("Tempo total:", sum(self.tempos.values()))
