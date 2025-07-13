#emprestimo, valor da casa, salario, anos a pagar, prestação mensal nao exceder 30% do salario
casa = float(input("valor da casa: R$ "))
salario = float(input("Salário: R$ "))
anos = int(input("Em quantas anos deseja pagar? R$ "))
prestação = casa / (anos * 12)
minimo = salario * 30 /100

if prestação >= minimo:
    print("\033[31mNEGADO!!\033[m\nPara pagar uma casa de R$ {} em {} anos "
          "\na prestação será de R$ {:.2f} e excede seu sálario de R$ {:.2f}".format(casa,anos,prestação, salario))
else:
    print("\033[32mAPROVADO!!\033[m\nPara pagar uma casa de R$ {} em {} anos "
          "\na prestação será de R$ {:.2f} e é compativél com seu sálario de R$ {:.2f}".format(casa, anos,prestação, salario))

#print("{:.2f}  {:.2f}  {:.2f}  {:.2f}".format(casa, salario, anos, prestação))
