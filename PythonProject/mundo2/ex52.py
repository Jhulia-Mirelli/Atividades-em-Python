#ler se o numero é primo
n = int(input("Digite um valor: "))
cont = 0
for c in range(1,n+1):
    if n % c == 0:
        cont += 1
if cont == 2:
    print("{} É UM NÚMERO PRIMO".format(n))
else:
    print("{} NÃO É UM NUMERO PRIMO".format(n))
