from numero import Numero


numero = Numero()
#Diferentes formas, sobrecarregadas, de somar um valor
print(f"Número: {numero.getValor()}")
numero.somar()
print(f"Número: {numero.getValor()}")
numero.somar(10.5)
print(f"Número: {numero.getValor()}")
