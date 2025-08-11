class Numero:
    __valor = 0.0

    def getValor(self):
        return self.__valor

    def somar(self, valor = 1):
        self.__valor += valor