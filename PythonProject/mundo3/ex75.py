lista=()
par=()
num3 = 0
for c in range(0,4):
    valor=int(input("Digite um valor: "))
    lista += (valor,)
    if valor % 2== 0:
        par +=(valor,)
    if lista.count(3) > 0:
        num3 = lista.index(3)+1
print(lista)
print(f"Apareceu {lista.count(9)}x o valor 9")
print(f"Valores par digitados: {par}")
if num3 != 0:
    print(f"O primeiro valor 3 foi digitado na posição {num3}")
else:
    print("Não há registros do valor 3!!")





