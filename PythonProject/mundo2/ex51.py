#progressão aritmetica ler razão, mostrar 10 primeiros termos primeiro termo soma com razão
n1 = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
print(n1,end=' ')
for c in range(1,10):
    n1 = n1 + razao
    print(n1,end=" ")
