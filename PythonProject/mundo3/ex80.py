#colocar 5 numeros em ordem sem usar o sorted
lista = []
for cont in range(0,5):
    n = int(input("Digite um valor:"))
    if cont == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n < lista[pos]:
                lista.insert(pos,n)
                break
            pos +=1
print(lista)
'''print(lista)
for i in range(len(lista)):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            # variável auxiliar para fazer a troca
            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux

print("Lista ordenada:", lista)'''
