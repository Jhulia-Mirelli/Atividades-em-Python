# input de varios valores em uma lista se já tiver numero igual nao add, mostrar todos os valores em ordem
from itertools import repeat

lista = []
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
    else:
        while n in lista:
            print("O número já está registrado, digite outro....")
            n = int(input("Digite um valor: "))
        lista.append(n)
    res = str(input("Deseja continuar? [S]Sim [N]Não")).upper().strip()[0]
    if res == 'N':
        break
print(sorted(lista))