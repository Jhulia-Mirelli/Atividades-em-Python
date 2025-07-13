
#caixa eletronico, valor a ser sacado int, print os valores a serem entregue(50,20,10,1)
valor = int(input("Qual valor você deseja sacar? R$"))
tot50= tot20= tot10= tot1= 0
while True:
    if valor >= 50:
        while valor >= 50:
            valor -= 50
            tot50 += 1
        print(f'Total de {tot50} cédulas de R$50 reais')
    if valor < 50 and valor >= 20:
        while valor < 50 and valor >=20:
            valor -= 20
            tot20 += 1
        print(f'Total de {tot20} cédulas de R$20 reais')
    if valor < 20 and valor >=10:
        while valor < 20 and valor >=10:
            valor -= 10
            tot10 += 1
        print(f'Total de {tot10} cédulas de R$10 reais')
    if valor < 10 and valor >= 1:
        while valor < 10 and valor >=1:
            valor -= 1
            tot1 += 1
        print(f'Total de {tot1} cédulas de R$1 real')
    if valor == 0:
        break

