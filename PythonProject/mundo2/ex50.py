#soma de 6 num inteiros e mostre a soma apenas do pares
soma = 0
cont = 0
for c in range(1,7):
    n = int(input("Digite um valor: "))
    if n % 2 ==0:
        soma += n
        cont += 1
print("Soma dos {} valores inteiros: {}".format(cont, soma))