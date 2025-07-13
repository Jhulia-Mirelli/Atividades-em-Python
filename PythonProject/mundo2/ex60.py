#fatorial
n = int(input("Digite um valor: "))
cont = n
fatorial = n
print(n, end="")
while cont > 1:
    cont -= 1
    fatorial *= cont
    print("x{}".format(cont), end="")
print("={}".format(fatorial))