from operacoes import Adicao, Subtracao
from random import random


operacoes = []
operacoes.append(Adicao())
operacoes.append(Subtracao())

a = random()*100
b = random()*100
resultado = 0.0

for om in operacoes:
    resultado = om.calcular(a, b)
    print(f"{a} {om.getOperador()} {b} = {resultado}")
