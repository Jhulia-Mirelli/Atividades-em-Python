from random import randint
lista = ()
maior = 0
menor = 0
for c in range(0,5):
    n = randint(1,10)
    lista +=(n,)
for c in range(len(lista)):
    if c == 0:
        maior = lista[c]
        menor = lista[c]
    elif lista[c] > maior:
        maior = lista[c]
    elif lista[c] < menor:
        menor = lista[c]
print(lista)
print(f"Maior valor: {maior}, Menor valor: {menor}")