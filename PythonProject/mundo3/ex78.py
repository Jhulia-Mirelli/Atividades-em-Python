#criar lista com 5 elementos, mostrar maior e menor, e as posiçoes
lista = []
maior = menor =0
for cont in range(0,5):
    lista.append(int(input("Digite um valor: ")))
    maior=max(lista)
    menor =min(lista)
print(lista)
print(f"Maior valor é {max(lista)} na posição: ", end=" ")
for i,n in enumerate(lista):
    if n == maior and lista.count(n) >= 1:
        print(f"{i+1}...", end=" ")
print(f"\nMenor valor é {min(lista)} na posição: ", end=" ")
for i,n in enumerate(lista):
    if n == menor and lista.count(n) >= 1:
        print(f"{i+1}...",end=" ")


