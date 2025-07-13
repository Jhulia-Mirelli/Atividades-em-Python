a = int(input())
b = int(input())
c = int(input())
#verificando o menor
menor = a #var
if b< a and b<c:
    menor = b
if c < a and c < b:
    menor = c
#verificando o maior
maior = a #var
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('Maior {}'.format(maior))
print('Menor {}'.format(menor))