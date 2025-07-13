#leia o nome e mostre o primeiro e ultimo

nome = str(input('Digite seu nome: ')).strip()
print('Nome: ', nome)
print('Primeiro Nome: ',nome.split()[0])
print('Segundo Nome: ',nome.split()[-1])
