class Carro:
    __rpm = 0
    __velocidade = 0
    __ligado = False

    def ligar(self):
        self.__ligado = True

    def desligar(self):
        # Desligar apenas se o carro estiver parado
        if self.__velocidade == 0:
            self.__ligado = False

    def getVelocidade(self):
        return self.__velocidade

    def acelerar(self):
        # Acelerar até um limite de velocidade,
        # quando o carro estiver ligado
        if self.__ligado and self.__velocidade < 100:
            self.__rpm += 1
            self.__velocidade += 10

    def frear(self):
        # Carro parado não precisa ser freado
        if self.__ligado and self.__velocidade > 0:
            self.__rpm -= 1
            self.__velocidade -= 10
