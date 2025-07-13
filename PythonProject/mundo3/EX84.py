lista = list()
while True:
    dados = [str(input("Digite seu nome: ")), float(input("Digite seu peso: "))]
    lista.append(dados[:])
    dados.clear()
    res = str(input("Deseja continuar cadastrando? [S]Sim [N]Não")).upper().strip()[0]
    while res not in "SN":
        print("\033[31mresposta inválida!\033[m")
        res = str(input("Deseja continuar cadastrando? [S]Sim [N]Não")).upper().strip()[0]
    if res == "N":
        print(lista)
        print(f"Total de pessoas cadastradas: {len(lista)}")
        break
maior = menor = 0
for p in range(len(lista)):
    peso = lista[p][1]
    if p == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
nome1 = []
nome2 = []
for p in range(len(lista)):
    n = lista[p][0]
    if lista[p][1] == maior:
        nome1.append(n)
    if lista[p][1] == menor:
        nome2.append(n)
print(f"Menor peso é {menor}Kg. Registros com esse peso: {nome2}")
print(f"Maior peso é {maior}Kg. Registros com esse peso: {nome1}")
