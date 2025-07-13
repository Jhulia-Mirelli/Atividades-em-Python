# trinagulo equilátero, isosceles, escaleno
a = int(input("valor: "))
b = int(input("valor: "))
c = int(input("valor: "))
if (a + b) > c and (b + c) > a and (c + a) > b:
    print("Forma um triângulo")
    if (a == b) and (b == c): #a == b == c (pode ser feito assim)
        print("Triângulo Equilátero")
    elif (a == b) or (b == c) or (c == a): #poderia colocar em um else para diminuir código
        print("Triângulo Isósceles")
    elif (a != b) and (b != c):
        print("Triângulo Escaleno") #a != b != c != a
else:
    print("Não forma um triângulo")