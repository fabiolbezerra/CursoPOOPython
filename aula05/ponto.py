from math import sqrt, pow


class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def distancia(self, xOuPonto, y = None):
        valorX = 0.0
        valorY = 0.0
        if y == None:
            #Assume que xOuPonto é um ponto
            valorX = xOuPonto.getX()
            valorY = xOuPonto.getY()
        else:
            #Assume que xOuPonto é x
            valorX = xOuPonto
            valorY = y

        quadradoDiferencaX = pow(self.__x - valorX, 2)
        quadradoDiferencaY = pow(self.__y - valorY, 2)
        distancia = sqrt(quadradoDiferencaX + quadradoDiferencaY)
        return distancia