#calculando area com função
def area (a,b):
    r = a * b
    print(f"A área de um terreno {a}x{b} é de {r}m²")


print("controle de terreno")
print("-"*30)
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l,c)
