from modelos.produto import Produto

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def getTempoDeBateria(self):
        return self.__tempoDeBateria

    def setTempoDeBateria(self, tempo):
        self.__tempoDeBateria = tempo

    def getInformacoes(self):
        base_info = super().getInformacoes()
        return f"{base_info}, Tempo de Bateria: {self.__tempoDeBateria} horas"

    def cadastrar(self):
        print("Notebook cadastrado com sucesso.")
