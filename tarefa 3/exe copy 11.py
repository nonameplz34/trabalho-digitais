salario = float(input("quanto recebe? "))

aumentode20 = 20
aumentode15 = 15
aumentode10 = 10
aumentode5 = 5

quantoAumentou = salario/10

valortotal = salario + quantoAumentou

texto = "antes seu salario era", salario, "o percentual aplicado é de "
texto1 = " um aumento de ", quantoAumentou, "um total de ",

if salario <= 280:
    print(texto, aumentode20 , " um aumento de ", salario/100*aumentode20, "totalizando ", salario/100 * aumentode20 + salario)
elif salario > 280 and salario <= 700:
    print(texto, aumentode15 , " um aumento de ", salario/100*aumentode15,  "totalizando ",salario/100  * aumentode15+ salario)
elif salario >700 and salario <= 1500:
    print(texto, aumentode10 , " um aumento de ", salario/100*aumentode10, "totalizando ", salario/100 * aumentode10+ salario)
else:
    print(texto, aumentode5 , " um aumento de ", salario/100*aumentode5, "totalizando ", salario/100 * aumentode5+ salario)


# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.