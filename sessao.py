class SessaoJogo:
    def __init__(self, jogo, tempo, total):
        self.jogo = jogo
        self.tempo = tempo
        self.total = total

    def status(self):
        if self.total < 2:
            return "iniciado"
        elif self.total < 10:
            return "em andamento"
        elif self.total < 20:
            return "muito jogado"
        else:
            return "concluido"

    def linha(self):
        return f"{self.jogo.titulo};{self.tempo};{self.total};{self.status()}"