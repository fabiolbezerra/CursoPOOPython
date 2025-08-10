class Pessoa:
    def __init__(self):
        self.__nome = ""

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome


class Professor(Pessoa):
    def __init__(self):
        self.__salario = 0.0

    def getSalario(self):
        return self.__salario

    def setSalario(self, salario):
        self.__salario = salario


class Aluno(Pessoa):

    def __init__(self):
        self.__matricula = ""

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula