#tupla unica de produto e preços, print uma listagem com preço e nome do produto
lista = ("Lápis", 1.99, "Caderno", 2, "Borracha", 3)
print("-"*40)
print(f"{' LISTAGEM DE PREÇOS ':^40}")
print("-"*40)
for cont in range (0,len(lista)):
    if cont % 2 != 0:
        print(f"{lista[cont]:<7.2f}",end="\n")
    if cont % 2 ==0:
        print(f"{lista[cont]:.<30}",end="R$")
