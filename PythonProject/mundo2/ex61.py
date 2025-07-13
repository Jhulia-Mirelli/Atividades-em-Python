#progressão aritmetica ler razão, mostrar 10 primeiros termos primeiro termo soma com razão
p1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
cont = 50
print(p1, end=" ")
while cont != 0:
    p1 = p1 + razao
    cont -= 1
    print(p1, end=" ")