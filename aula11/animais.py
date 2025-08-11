from abc import ABC, abstractmethod


class Animal(ABC):
    __nome = ""

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    @abstractmethod
    def movimentar(self, distancia):
        pass


class Gato(Animal):
    def movimentar(self, distancia):
        print(f"{self.getNome()} andando {distancia}")


class Peixe(Animal):
    def movimentar(self, distancia):
        print(f"{self.getNome()} nadando {distancia}")
