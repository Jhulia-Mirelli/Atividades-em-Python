#ler o peso de 5 pessoas e mostra a mais pesada e a mais leve
maior = 0
menor = 0
for c in range(0,5):
    peso = float(input("Digite o peso: "))
    if c == 1:    #alocando apenas no primeiro laço os valores de peso, para não ter que usar 99999 no menor
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("Maior peso: {}Kg\nMenor peso: {}Kg".format(maior,menor))