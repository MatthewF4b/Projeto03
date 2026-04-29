from steampy import SteamPy

sistema = SteamPy()


def menu():
    while True:
        print("""
1 - Carregar catálogo
2 - Listar jogos
3 - Buscar jogo
4 - Adicionar ao backlog
5 - Ver backlog
6 - Jogar próximo
7 - Ver recentes
8 - Registrar tempo de jogo
9 - Dashboard
10 - Recomendar
0 - Sair
""")

        op = input("Escolha: ")

        if op == "1":
            sistema.carregar_jogos("dataset.csv")

        elif op == "2":
            sistema.listar()

        elif op == "3":
            nome = input("Digite o nome: ")
            sistema.buscar(nome)

        elif op == "4":
            id_jogo = int(input("ID do jogo: "))
            sistema.adicionar_backlog(id_jogo)

        elif op == "5":
            sistema.backlog.mostrar()

        elif op == "6":
            sistema.jogar_proximo()

        elif op == "7":
            sistema.recentes.mostrar()

        elif op == "8":
            jogo = sistema.recentes.topo()
            if jogo:
                tempo = float(input("Horas jogadas: "))
                sistema.registrar_tempo(jogo, tempo)
            else:
                print("Nenhum jogo recente")

        elif op == "9":
            sistema.dashboard()

        elif op == "10":
            sistema.recomendar()

        elif op == "0":
            print("Saindo...")
            break


menu()