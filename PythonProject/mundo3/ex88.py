#mega sena, gerar 6 num de 1-60
from random import randint
from time import sleep
lista = list()
cont = 0
res = int(input("Quantos jogos deseja realizar? "))
while cont != res:
    n = [randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60)]
    if n not in lista:
        lista.append(n[:])
        n.clear()
        cont+=1
print(f'{"Sorteando Jogos":^30}')
for i in range(0,res):
    print(f"Jogo {i+1}°: {lista[i]}")
    sleep(1)
