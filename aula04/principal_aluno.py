from aluno import Aluno

#A quantidade de objetos alunos independe da existência de um objeto Aluno
print(f"Total de alunos (c): {Aluno.getTotalDeAlunos()}")

#Criando um objeto Aluno
fulano = Aluno('20250001')
#Apresentando a quantidade de objetos a partir da classe (c) e da instância (i)
print(f"Total de alunos (c): {Aluno.getTotalDeAlunos()}")
print(f"Total de alunos (i): {fulano.getTotalDeAlunos()}")

#Criando outro objeto Aluno
ciclano = Aluno('20250002')
#Apresentando a quantidade de objetos a partir da classe (c) e da instância (i)
print(f"Total de alunos (c): {Aluno.getTotalDeAlunos()}")
print(f"Total de alunos (i): {ciclano.getTotalDeAlunos()}")