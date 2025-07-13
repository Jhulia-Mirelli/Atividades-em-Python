salario = float(input("Salário: "))
if salario <= 1250.00:
    salario = salario + (salario * (15/100))
else:
    salario = salario + (salario * 10/100)
print("Sal  ário ajustado R$ {}".format(salario))