class PilhaRecentes:
    def __init__(self, limite=20):
        self.dados = []
        self.limite = limite

    def push(self, jogo):
        # remove duplicado
        self.dados = [j for j in self.dados if j.id != jogo.id]

        self.dados.append(jogo)

        if len(self.dados) > self.limite:
            self.dados.pop(0)

    def topo(self):
        if self.is_empty():
            return None
        return self.dados[-1]

    def is_empty(self):
        return len(self.dados) == 0

    def tamanho(self):
        return len(self.dados)

    def mostrar(self):
        if self.is_empty():
            print("Nenhum jogo recente")
            return

        print("\n--- RECENTES ---")
        for jogo in reversed(self.dados):
            print(jogo.exibir())
