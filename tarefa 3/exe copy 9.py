Numero1 = int(input("primeira numero: "))
Numero2 = int(input("Segundo numero: "))
Numero3 = int(input("Terceiro numero: "))


if Numero1 < Numero2 and Numero1 < Numero3 and Numero2 <Numero3:
    print("o primeiro é ")
    print(Numero1)
    print("segundo")
    print(Numero2)
    print("e ultimo ")
    print(Numero3)
elif Numero1 < Numero2 and Numero1 < Numero3 and Numero2 >Numero3:
    print("o primeiro é ")
    print(Numero1)
    print("segundo")
    print(Numero3)
    print("e ultimo ")
    print(Numero2)

if Numero2 < Numero1 and Numero2 < Numero3 and Numero1 <Numero3:
    print("o primeiro é ")
    print(Numero2)
    print("segundo")
    print(Numero1)
    print("e ultimo")
    print(Numero3)
elif Numero2 < Numero1 and Numero2 < Numero3 and Numero1 >Numero3:
    print("o primeiro é ")
    print(Numero2)
    print("segundo")
    print(Numero3)
    print("e ultimo")
    print(Numero1)

if Numero3 < Numero2 and Numero3 < Numero1 and Numero1 <Numero2:
    print("o primeiro é ")
    print(Numero3)
    print("segundo")
    print(Numero1)
    print("e ultimo")
    print(Numero2)
elif Numero3 < Numero2 and Numero3 < Numero1 and Numero1 >Numero2:
    print("o primeiro é ")
    print(Numero3)
    print("segundo")
    print(Numero2)
    print("e ultimo")
    print(Numero1)


