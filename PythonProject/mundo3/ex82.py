lista = []
par = []
impar = []

while True:
    n = int(input("Digite uma valor: "))
    lista.append(n)
    res = str(input("Deseja continuar? [S]Sim [N]Não ")).upper().strip()[0]
    while res not in "SN":
        res = str(input("Deseja continuar? [S]Sim [N]Não ")).upper().strip()[0]
    if res == "N":
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(lista)
print(par)
print(impar)