from random import randint
def somaPar(lista):
    soma=0
    for c in lista:
        if c % 2 == 0:
            soma+=c
    print(f"Soma dos valores pares: {soma}")
def sorteia(lista):
    for c in range(0,5):
        lista.append(randint(1,10))
    print(f"Valores:", end=" ")
    for c in lista:
        print(c,end=" ")
    print()


numero=[]
sorteia(numero)
somaPar(numero)
