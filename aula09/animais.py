class Animal:

    def __init__(self):
        print("Criando o animal ...")
        self.especie = ""


class Gato(Animal):
    pelo = ""


class Peixe(Animal):
    def __init__(self):
        print("Criando o peixe ...")
        self.escama = ""
        #O que acontece se comentar a linha abaixo?
        super().__init__()
