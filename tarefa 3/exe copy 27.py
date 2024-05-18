kilos = float(input("escolha quantos kilos de morango"))
kilos2 = float(input("escolha quantos kilos de maça"))

preço1 = kilos * 2.50
preço2 = kilos2 * 1.80
valortotal =preço1 + preço2


if kilos + kilos2 > 8 or valortotal > 25 :
    print("vc ganhou um desconto de 10 porcent0, sua compra foi para", valortotal/100 * 10 ) 
else:
    print("vc nºa ganhou um desconto")