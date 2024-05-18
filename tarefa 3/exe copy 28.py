
escolha = float(input("qualcarne, (0)File Duplo(1)Alcatra (2)Picanha "))
kilos = float(input("escolha quantos kilos"))

metodo = float(input("forma depagamentpo, (0)dinheiro (1?cartºao "))


if escolha == 0  :
    valortotal = kilos * 4.90
elif escolha == 1  :
    valortotal = kilos * 5.90
else :
    valortotal = kilos * 6.90

if escolha == 1  :
        if metodo == 1  :
            print("vc ganhou um desconto de 10 porcent0, sua compra foi para", valortotal/100 * 10 ) 
        else:
            print("sem desconto") 
    
else:
    print("resposta invalida ")