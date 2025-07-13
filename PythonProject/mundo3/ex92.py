#nome, ano nasc, carteira, se tiver salario e ano de contratação dve ser a primeria, print valor aposentadoria,35 anos de colaboração
from datetime import date
pessoa = {}
pessoa['nome'] = str(input("Nome: "))
i = int(input("Ano de nascimento: "))
pessoa['idade'] = (date.today().year - i)
pessoa['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))
if pessoa['ctps'] > 0:
    a = int(input("Ano da primeira contratação: "))
    pessoa['contratação'] = a
    ap = (35 - (date.today().year - a)) + pessoa['idade']
    pessoa['aposentadoria'] = ap
    pessoa['salario'] = float(input("Sálario: "))
else:
    del pessoa['ctps']
print(pessoa)