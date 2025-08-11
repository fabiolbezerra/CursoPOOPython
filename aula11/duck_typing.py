class Pato:
    def comer(self):
        print("Pato comendo")

    def voar(self):
        print("Pato voando")


class Pardal:
    def comer(self):
        print("Pardal comendo")

    def voar(self):
        print("Pardal voando")


class Baleia:
    def comer(self):
        print("Baleia comendo")

    def nadar(self):
        print("Baleia nadando")

animais = [Pato(), Pardal(), Baleia()]
for animal in animais:
    animal.comer()
    #Baleias não voam
    #animal.voar()