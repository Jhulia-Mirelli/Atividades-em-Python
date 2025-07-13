a = float(input("primeiro valor: "))
b = float(input("segundo valor: "))
c = float(input("terceiro valor: "))
#soma de quaisquer 2 lados deve ser maior que o terceiro

if ((a + b) > c) and ((b + c) > a) and ((c + a) > b):
    print("Forma um triângulo")
else:
    print("Não forma um triângulo")