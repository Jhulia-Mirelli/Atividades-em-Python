coloc20 = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
            'Onze', 'Doze', 'Treze', 'Quatorze', 'Chapecoense', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print("5 Primeiros colocados: ", end="") #print(coloc20[0:5])
for c in range(0,5):
    print(coloc20[c], end=",")
print("\n4 últimos colocados: ", end="") #print(coloc20[16:])[-4:]
for c in range(16,21):
    print(coloc20[c], end=",")

print("\nLista em ordem alfabetica\n",sorted(coloc20))

print("Chapeconse se encontra na posição: ",coloc20.index('Chapecoense')+1)
