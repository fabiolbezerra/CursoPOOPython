from carro import Carro


fusca = Carro()
print(f"Velocidade: {fusca.getVelocidade()}")
fusca.ligar()
print(f"Velocidade: {fusca.getVelocidade()}")
fusca.acelerar()
print(f"Velocidade: {fusca.getVelocidade()}")
fusca.frear()
print(f"Velocidade: {fusca.getVelocidade()}")
fusca.desligar()
print(f"Velocidade: {fusca.getVelocidade()}")