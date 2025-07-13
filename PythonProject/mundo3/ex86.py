matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(len(matriz)):
    for c in range(len(matriz)):
        matriz[l][c] = int(input(f"[{l}][{c}]"))
print()
for l in range(len(matriz)):
    for c in range(len(matriz)):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()
