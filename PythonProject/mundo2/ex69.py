#idade homem, mulher, pessoal mairo de 18, quant homem, mulher menos de 20
totidade = tothomem = totmulher = 0
while True:
    idade = int(input("Informe sua idade: "))
    sexo = str(input("Informe sexo [M]Mulher [H]Homem: ")).strip()[0].upper()
    while sexo !="M" and sexo != "H":
        sexo = str(input("Informe sexo [M]Mulher [H]Homem: ")).strip()[0].upper()
    res = str(input("Deseja continuar cadastrando? ")).strip()[0].upper()
    print("-"*20)
    while res != "S" and res != "N":
        res = str(input("Deseja continuar cadastrando? ")).strip()[0].upper()
    if idade >= 18:
        totidade+=1
    if sexo == "H":
        tothomem += 1
    if sexo == "M" and idade < 20:
        totmulher += 1
    if res == "N":
        print(f"Total pessoas (+18) cadastradas: {totidade}\nTotal homens cadastrados: {tothomem}\nTotal mulheres (-20) cadastrada: {totmulher}")
        break
