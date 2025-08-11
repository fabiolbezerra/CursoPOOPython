from ponto import Ponto


a = Ponto(1, 1.5)
b = Ponto(5, 4.5)
#Duas formas de calcular a distância
print(f"Distância entre a e b: {a.distancia(b):.2}")
x = b.getX()
y= b.getY()
print(f"Distância entre a e b: {a.distancia(x, y):.2}")