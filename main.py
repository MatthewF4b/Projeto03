from steampy import SteamPy

sistema = SteamPy()


def menu():
    while True:
        print("""
1. Carregar catálogo
2. Listar jogos
3. Buscar jogo por nome
4. Filtrar por gênero
5. Filtrar por console
6. Filtrar por nota
7. Ordenar catálogo
8. Adicionar jogo ao backlog
9. Ver backlog
10. Jogar próximo do backlog
11. Ver jogos recentes
12. Retomar último jogo
13. Registrar tempo de jogo
14. Ver histórico completo
15. Ver recomendações
16. Ver ranking pessoal
17. Ver dashboard
18. Salvar backlog
19. Sair
""")

        op = input("Escolha: ")

        if op == "1":
            sistema.carregar_jogos("dataset.csv")

        elif op == "2":
            sistema.listar()

        elif op == "3":
            sistema.buscar(input("Nome: "))

        elif op == "4":
            sistema.filtrar_genero(input("Gênero: "))

        elif op == "5":
            sistema.filtrar_console(input("Console: "))

        elif op == "6":
            sistema.filtrar_nota(float(input("Nota mínima: ")))

        elif op == "7":
            print("Critérios: titulo | nota | vendas")
            sistema.ordenar(input("Escolha: "))

        elif op == "8":
            sistema.adicionar_backlog(int(input("ID: ")))

        elif op == "9":
            sistema.backlog.mostrar()

        elif op == "10":
            sistema.jogar_proximo()

        elif op == "11":
            sistema.ver_recentes()

        elif op == "12":
            sistema.retomar()

        elif op == "13":
            jogo = sistema.recentes.topo()
            if jogo:
                tempo = float(input("Horas jogadas: "))
                sistema.registrar_tempo(jogo, tempo)
            else:
                print("Nenhum jogo ativo")

        elif op == "14":
            sistema.ver_historico()

        elif op == "15":
            sistema.recomendar()

        elif op == "16":
            sistema.ranking()

        elif op == "17":
            sistema.dashboard()

        elif op == "18":
            sistema.salvar_backlog()

        elif op == "19":
            print("Saindo...")
            break


menu()
