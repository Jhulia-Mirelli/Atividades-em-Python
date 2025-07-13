matriz = [[[0],[0],[0],],[[0],[0],[0]],[[0],[0],[0]]]
soma3 = somapar = maior2=0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i][j] = int(input(f"[{i}][{j}]: "))
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
        if j == 2:
            soma3 += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior2:
                maior2 = matriz[i][j]

for l in range(len(matriz)):
    for c in range(len(matriz)):
        print(f"[{matriz[l][c]:^5}]",end="")
    print()
print(f"Soma de todos os valores pares: {somapar}")
print(f"Soma dos valores da 3 Coluna: {soma3}")
print(f"O maior valor da 2° linha é {maior2}")
