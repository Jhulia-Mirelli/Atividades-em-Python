#programa que msotre os valores pares entre 1 50
for c in range(1,51):
    if c % 2 == 0:
        print(c, end=" ")
print("\n")
#ou
for c in range(2,51,2): #<<o programa trabalha menos assim
        print(c, end=" ")