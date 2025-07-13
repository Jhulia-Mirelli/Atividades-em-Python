from _datetime import date
ano = int(input("Digite o ano ou digite 0 para analisar ano atual..."))
if ano == 0:
    ano = date.today().year
if ano % 100 == 0 and ano % 400 != 0 or ano % 4 != 0:
    print("{} Não é um ano Bissexto".format(ano))
else:
    print("{} Ano Bissexto".format(ano))