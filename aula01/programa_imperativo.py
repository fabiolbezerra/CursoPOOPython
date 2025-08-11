print("Olá mundo!")
nota1 = float(input("Qual a sua nota na primeira prova? "))
nota2 = float(input("Qual a sua nota na segunda prova? "))
media = (nota1 + nota2) / 2
if media >= 6:
    print("Aprovado!")
else:
    print("Vai para recuperação.")
