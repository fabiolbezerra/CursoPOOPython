class Animal:
    def movimentar(self, distancia):
        print("Animal se movimentando", distancia)


class Gato(Animal):
    def movimentar(self, distancia):
        print("Gato andando", distancia)


class Peixe(Animal):
    def movimentar(self, distancia):
        print("Peixe nadando", distancia)
