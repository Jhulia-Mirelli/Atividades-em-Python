#tupla numero extenso 0 20, ler int mostrar extenso
contagem = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
            'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input("Digite um valor [0 à 20]: "))
while num < 0 or num > 20:
    num = int(input("Digite um valor [0 à 20]: "))
print(contagem[num])
