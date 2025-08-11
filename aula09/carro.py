class Carro:
    modelo = ""
    cor = ""
    ano = 0
    placa = ""

    def __str__(self):
        return "Carro[modelo=" + self.modelo + ", cor=" + self.cor + ", placa=" + self.placa + "]"