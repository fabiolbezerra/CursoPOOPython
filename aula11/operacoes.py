from abc import ABC, abstractmethod


class OperacaoMatematica(ABC):
    def __init__(self, operador):
        self.__operador = operador

    def getOperador(self):
        return self.__operador

    @abstractmethod
    def calcular(self, a, b):
        pass


class Adicao(OperacaoMatematica):
    def __init__(self):
        super().__init__("+")

    def calcular(self, a, b):
        return a + b


class Subtracao(OperacaoMatematica):
    def __init__(self):
        super().__init__("-")

    def calcular(self, a, b):
        return a - b