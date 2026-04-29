def analisar_proximos(self):
    print("\n--- PRÓXIMOS JOGOS (BACKLOG) ---")
    self.backlog.mostrar()


def analisar_recentes(self):
    print("\n--- JOGOS RECENTES ---")
    self.recentes.mostrar()


def jogo_mais_jogado(self):
    if not self.tempos:
        print("Nenhum jogo jogado ainda")
        return

    jogo_id = max(self.tempos, key=self.tempos.get)
    jogo = self.catalogo[jogo_id]

    print("\nJogo mais jogado:")
    print(jogo.exibir(), "- Horas:", self.tempos[jogo_id])


def genero_favorito(self):
    contagem = {}

    for s in self.historico:
        g = s.jogo.genero
        contagem[g] = contagem.get(g, 0) + 1

    if not contagem:
        print("Sem dados ainda")
        return

    favorito = max(contagem, key=contagem.get)
    print("\nGênero favorito:", favorito)


def console_favorito(self):
    contagem = {}

    for s in self.historico:
        c = s.jogo.console
        contagem[c] = contagem.get(c, 0) + 1

    if not contagem:
        print("Sem dados ainda")
        return

    favorito = max(contagem, key=contagem.get)
    print("\nConsole mais jogado:", favorito)


def jogos_em_andamento(self):
    count = 0

    for tempo in self.tempos.values():
        if 2 <= tempo < 20:
            count += 1

    print("\nJogos em andamento:", count)


def media_notas(self):
    notas = []

    for s in self.historico:
        notas.append(s.jogo.critic_score)

    if not notas:
        print("Sem dados ainda")
        return

    media = sum(notas) / len(notas)
    print("\nNota média dos jogos jogados:", round(media, 2))


def panorama(self):
    print("\n--- PANORAMA GERAL ---")

    print("Total de jogos:", len(self.catalogo))
    print("Backlog:", self.backlog.tamanho())
    print("Recentes:", self.recentes.tamanho())
    print("Sessões:", len(self.historico))
    print("Tempo total:", sum(self.tempos.values()))

    self.genero_favorito()
    self.console_favorito()


def recomendacao_avancada(self):
    print("\n--- RECOMENDAÇÃO INTELIGENTE ---")

    generos = {}
    consoles = {}

    for s in self.historico:
        g = s.jogo.genero
        c = s.jogo.console

        generos[g] = generos.get(g, 0) + 1
        consoles[c] = consoles.get(c, 0) + 1

    if not generos:
        print("Sem dados suficientes")
        return

    genero_pref = max(generos, key=generos.get)
    console_pref = max(consoles, key=consoles.get)

    print("Baseado em:")
    print("- Gênero:", genero_pref)
    print("- Console:", console_pref)

    for jogo in self.catalogo:
        if (
            jogo.genero == genero_pref
            and jogo.console == console_pref
            and jogo.id not in self.tempos
        ):
            print("\nSugestão:")
            print(jogo.exibir())
            break
