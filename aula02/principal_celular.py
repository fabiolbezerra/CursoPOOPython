from celular import Celular

#Criando um celular
samsung = Celular()
#Apresentando o estado de um celular recém-criado
print(f"Ligado? {samsung.ligado}")
#Ligando o celular e apresentando o novo estado do mesmo
samsung.ligar()
print(f"Ligado? {samsung.ligado}")
#Desligando o celular e apresentando o novo estado do mesmo
samsung.desligar()
print(f"Ligado? {samsung.ligado}")