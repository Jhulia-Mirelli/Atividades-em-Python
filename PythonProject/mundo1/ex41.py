#categoria de acordo com idade
from _datetime import date
anonas = int(input("Digite o ano de seu nascimento: "))
idade = date.today().year - anonas
print("Idade: {}".format(idade))
if idade <= 9:
    print("Categoria MIRIM")
elif idade <= 14:
    print("Categoria INFANTIL")
elif idade <= 19:
    print("Categoria JUNIOR")
elif idade <=20:
    print("Categoria SÊNIOR")
else:
    print("Categoria MASTER")