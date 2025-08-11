from pessoas import Pessoa, Aluno, Professor


#lista admite qualquer tipo de objeto
pessoas = []

#Adicionando uma pessoa
pessoas.append(Pessoa())
pessoas[0].setNome("Fulano")

#Adicionando um aluno
pessoas.append(Aluno())
pessoas[1].setNome("Ciclano")
#não há casting, pois ciclano é um Aluno
pessoas[1].setMatricula("2025123")

#Adicionando um professor
pessoas.append(Professor())
pessoas[2].setNome("Beltrano")
#não há casting, pois beltrano é um Professor
pessoas[2].setSalario(1518)