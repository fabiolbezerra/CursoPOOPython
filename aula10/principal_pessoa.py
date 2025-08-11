from pessoas import Pessoa, Aluno, Professor


fulano = Pessoa()
fulano.setNome("Fulano")

ciclano = Aluno()
ciclano.setNome("Ciclano")
#não há casting, pois ciclano é um Aluno
ciclano.setMatricula("2025123")

beltrano = Professor()
beltrano.setNome("Beltrano")
#não há casting, pois beltrano é um Professor
beltrano.setSalario(1518)