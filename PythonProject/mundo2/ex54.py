#ler ano nascimento, fim mostrar quantas pessoas nao atigiram a maior idade
from datetime import date
maior = 0
menor = 0
for c in range(0,7):
    anonasc = int(input("Digite o ano de seu nascimento: "))
    idade = date.today().year - anonasc
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1

print("Total de pessoas maior de idade: {}\nTotal de pessoas menor de idade: {}".format(maior,menor))
