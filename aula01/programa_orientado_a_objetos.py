from jogador import Jogador

# Criando o objeto
j10 = Jogador()
# Definindo o estado do objeto
j10.nome = "Pelé"
j10.altura = 1.73
j10.peso = 73
j10.posicao = "Meia atacante"
#Apresentando o estado do objeto
print(j10.nome)
print(j10.posicao)
#Explorando o comportamento do objeto
j10.driblar()