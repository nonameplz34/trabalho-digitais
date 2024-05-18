
item1 = int(input("Qual o preço do quarda roupa?: "))
item2 = int(input("Qual o preço do computador?: "))
item3 = int(input("Qual o preço da TV?: "))

# lista = [item1, item2, item3 ]

# print("voce deveria comprar o ")
# print({min(lista)})

# OU COMO O EXERCICIO PEDE KKKKKKKKKKKK, FOI MAL

if item1 < item2 and item1 < item3 :
    print("compra o guarda roupa")

elif item2 < item1 and item2 < item3 :
    print("compra o computador")

else :
    print("compra a TV")