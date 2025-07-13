#ler 3 numero e mostrar o maior e o menor
a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor: "))
nummaior = 0
nummenor = 0
if (a > b) and (a > c):
    nummaior = a
    if b > c:
       nummenor = c
    else:
        nummenor = b
if (b > c) and (b > a):
    nummaior = b
    if c > a:
        nummenor = a
    else:
        nummenor = c
if (c > a) and (c > b):
    nummaior = c
    if b > a:
        nummenor = a
    else:
        nummenor = b
print(nummaior,nummenor)