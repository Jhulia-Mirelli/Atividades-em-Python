#ler nome, idade, sexo de 4 pessoas/media de idade/nome do homem mais velho/mulheres com menos de 20
nome = []
idade = []
sexo = []
totidade = 0
totmulher20 = 0
maioridhomem = 0
conthomem = 0
for c in range(0,4):
    print("------------{}°------------".format(c+1))
    n = str(input("Digite seu nome: "))
    nome.append(n)
    i = int(input("Digite sua idade: "))
    idade.append(i)
    totidade = totidade + i
    s = int(input("Com qual gênero você se identifica?\n[1] Mulher [2] Homem [3] Outro\nDigite: "))
    sexo.append(s)
    if s == 1 and i < 20:
        totmulher20 = totmulher20 + 1
    else:
        if s == 2:
            maioridhomem = i
            conthomem = c
print("Média de idade do grupo é de {:.0f} anos".format(totidade/4))
print("{} é o homem mais velho, com {} anos".format(nome[conthomem],maioridhomem))
print("Total de mulheres com menos de 20 anos: {}".format(totmulher20))