numero = float(input("escolha um numero"))
escolha = float(input("qual operaçºao quer fazer, (0)impa par(1)positivo negativo(2)inteiro decimal"))

if escolha == 0  :
        if numero % 2 != 0  :
            print("e impa ")
        else:
            print("e pa ")
    
elif escolha == 1  :
        if numero > 0  :
            print("e positivo ")
        else:
            print("e negativo ")
    
elif escolha == 2  :
    if numero % 1 == 0  :
        print("e inteiro ")
    else :
        print("e decimal ")
    
    
else:
    print("resposta invalida ")