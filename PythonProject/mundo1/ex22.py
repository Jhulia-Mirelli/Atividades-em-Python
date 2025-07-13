#leia um nome, mostre o nome com maiuscula, minusculas,total de letras,total de letras primeiro nome
nome = str(input("Digite seu nome: ")).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' ')) #tirando os espaços no meio do nome
#nome = nome.split()
#print(len(nome[0]))
print(len(nome.split()[0]))
