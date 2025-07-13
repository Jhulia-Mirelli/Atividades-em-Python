#nome de pessoa e se tem silva
nome = str(input('Digite seu nome: ')).strip()
#print("Seu nome tem silva? ",nome.lower().split().count('silva') == 1)
print("Seu nome tem silva? {}".format('SILVA'in nome.upper())) #in é um operador