nota1 = float(input("nota no primeiro bimestre (1 a 10): "))
nota2 = float(input("nota no segundoo(1 a 10) "))

media = (nota1 + nota2) / 2

if media <= 10 and media >= 9:
    print("conceito A")

elif media < 9 and media >= 7.5:
    print("conceito B")

elif media <7.5 and media >= 6:
    print("conceito C")

elif media <6 and media >= 4:
    print("conceito D")

else:
    print("conceito E")
