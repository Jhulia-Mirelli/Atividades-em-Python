matriz = [[[],[],[],],[[],[],[]],[[],[],[]]]

for c in range(len(matriz[0])):
    n = int(input(f"[0][{c}]: "))
    matriz[0][c].append(n)
for c in range(len(matriz[1])):
    n= int(input(f"[1][{c}]: "))
    matriz[1][c].append(n)
for c in range(len(matriz[2])):
    n = int(input(f"[2][{c}]: "))
    matriz[2][c].append(n)
for c in matriz[0]:
    print(c, end="")
print()
for c in matriz[1]:
    print(c, end="")
print()
for c in matriz[2]:
    print(c, end="")