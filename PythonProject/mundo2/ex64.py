#ler vários numeros e mostrar a soma deles
n = soma = tot= 0
n = int(input("Digite um valor [999 para parar]: "))
while n != 999:
    tot+=1
    soma += n
    n = int(input("Digite um valor [999 para parar]: "))
print(f"Você digitou {tot} e o total foi: {soma}")
