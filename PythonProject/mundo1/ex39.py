# program de alistamento conforme idade
from datetime import date

resposta = int(input("Você gostaria de se alista no Exército Brasileiro? [1]SIM [2]NÃO\nEscolha a opção: "))
if resposta == 1:

    anonasc = int(input("Digite o ano de seu nascimento: "))
    anoatual = date.today().year
    idade = anoatual - anonasc
    print('-'*50)
    print("Quem nasceu em {} tem {} anos em {}".format(anonasc, idade, anoatual))
    print('-' * 50)
    if idade < 18:
        print("Faltam {} anos para se alistar ao serviço militar\nAno de alistamento: {}".format(18 - idade,
                                                                                             (anoatual + (18 - idade))))
    elif idade > 18:
        print("Você deveria ter se alistado ha {} anos\nAno de alistamento: {}".format(idade - 18, (anoatual - (idade - 18))))
    elif idade == 18:
        print("Você está na idade de se alistar no serviço militar")

else:
    print("Ok, agradecemos sua resposta. Mas fique atento(a), busque mais informações sobre as diretrizes a respeito do alistamento obrigatório!!")