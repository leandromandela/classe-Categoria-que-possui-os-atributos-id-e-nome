from modelos.produto import Produto

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    def getPotenciaDaFonte(self):
        return self._potenciaDaFonte

    def setPotenciaDaFonte(self, potencia):
        self._potenciaDaFonte = potencia

    def getInformacoes(self):
        base_info = super().getInformacoes()
        return f"{base_info}, Potência da Fonte: {self._potenciaDaFonte}W"

    def cadastrar(self):
        print("Desktop cadastrado com sucesso.")
