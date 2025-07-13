#ler valores int, mostrar média, maior e menor
res = 1
maior = menor = tot = soma=0
while res == 1:
    num = int(input("Digite um valor"))
    res = int(input("Deseja continuar? [1]SIM [2]NÃO"))
    tot += 1
    soma+=num
    if num < menor or menor == 0:
        menor = num
    if num > maior:
        maior = num

print("\nTotal de números digitados: {}\nMaior valor digitado: {}\nMenor valor digitado: {}\nMédia dos valores: {:.2f}".format(tot,maior, menor,soma/tot))
