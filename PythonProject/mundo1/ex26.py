#ler frase, total de 'a', posição q aparece primeira vez e por ultimo
frase = str(input('Digite frase: ')).strip().lower()
print("Quantidade de A's:",frase.count('a'))
print("localização primeiro A: ",frase.find('a')+1)
print("Localização último A: ",frase.rfind('a')+1)


