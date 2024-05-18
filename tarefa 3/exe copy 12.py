salario = float(input("quanto recebe? "))
hora = float(input("quantas horas trabalga? "))

SalarioBruto = salario*hora

irPara0 = SalarioBruto*0/100

irPara5 = 5
irPara10 = 15
irPara20 = 20

inss = SalarioBruto *10/100
fgts=  SalarioBruto *11/100

texto = "antes seu salario bruto era", SalarioBruto, "valor do IR "


if salario <= 900:
    print(texto, irPara0 , " INSS ",inss, "FGTS ", fgts, "total de descontos", irPara0+inss+fgts, "sobrou ", SalarioBruto- irPara0-inss-fgts  )
elif salario > 900 and salario <= 1500:
    print(texto, irPara5 , " INSS ", inss,  "FGTS ", fgts, "total de descontos", irPara5+inss+fgts, "sobrou ", SalarioBruto- irPara5-inss-fgts )
elif salario >1500 and salario <= 2500:
    print(texto, irPara10 , " INSS ", inss, "FGTS ", fgts, "total de descontos", irPara10+inss+fgts, "sobrou ", SalarioBruto- irPara10-inss-fgts  )
else:
    print(texto, irPara20 , " INSS ", inss,"FGTS ", fgts, "total de descontos", irPara20+inss+fgts, "sobrou ", SalarioBruto- irPara20-inss-fgts  )

