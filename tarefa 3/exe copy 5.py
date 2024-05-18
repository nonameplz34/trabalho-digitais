nota1 = float(input("primeira nota: "))
nota2 = float(input("segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("aprovado com Distinção")
elif media >= 7:
    print("aprovado")
else:
    print("reprovado")