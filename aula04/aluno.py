class Aluno:
    __totalDeAlunos = 0

    def __init__(self, matricula):
        self.__matricula = matricula
        Aluno.__totalDeAlunos += 1

    def getMatricula(self):
        return self.__matricula

    #Forma de criação de método de classe no Python, a partir de um decorador
    @classmethod
    def getTotalDeAlunos(cls):
        return Aluno.__totalDeAlunos