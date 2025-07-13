#dicionário ler nome e média mostrar se ta aprovado ou não
aluno = {}
aluno['Nome'] = str(input("Nome: "))
aluno['Média'] = float(input("Média do aluno: "))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 6 <= aluno['Média'] < 7 :
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for i,a in aluno.items():
    print (f'{i} é igual {a}')