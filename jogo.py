class Jogo:
    def __init__(self, id_jogo, titulo, console, genero, publisher, developer,
                 critic_score, total_sales, na_sales, jp_sales, pal_sales,
                 other_sales, release_date):

        self.id = id_jogo
        self.titulo = titulo
        self.console = console
        self.genero = genero
        self.publisher = publisher
        self.developer = developer

        # tratamento simples (nível júnior)
        try:
            self.critic_score = float(critic_score)
        except:
            self.critic_score = 0.0

        try:
            self.total_sales = float(total_sales)
        except:
            self.total_sales = 0.0

        try:
            self.na_sales = float(na_sales)
        except:
            self.na_sales = 0.0

        try:
            self.jp_sales = float(jp_sales)
        except:
            self.jp_sales = 0.0

        try:
            self.pal_sales = float(pal_sales)
        except:
            self.pal_sales = 0.0

        try:
            self.other_sales = float(other_sales)
        except:
            self.other_sales = 0.0

        self.release_date = release_date

    # 🔥 AQUI ESTÁ A CORREÇÃO PRINCIPAL
    def exibir(self):
        return (
            f"{self.id} - {self.titulo} | "
            f"Gênero: {self.genero} | "
            f"Console: {self.console} | "
            f"Nota: {self.critic_score} | "
            f"Vendas: {self.total_sales}"
        )
