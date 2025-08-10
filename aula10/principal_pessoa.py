from pessoas import Pessoa, Aluno, Professor


fulano = Pessoa()
fulano.setNome("Fulano")
print(fulano.getNome(), '\n')

ciclano = Aluno()
ciclano.setNome("Ciclano")
ciclano.setMatricula("2025123")
print(ciclano.getNome())
print(ciclano.getMatricula(), '\n')

beltrano = Professor()
beltrano.setNome("Beltrano")
beltrano.setSalario(1518)
print(beltrano.getNome())
print(beltrano.getSalario(), '\n')