
#posso usar from math import trunc
#exercício 16
'''num = float(input('Digite um valor: '))
print('O número {} tem sua parte inteira: {}'.format(num, math.trunc(num)))'''


# calculo da hipotenusa 1
'''a = float(input('Digite um valor: '))
b = float(input('Digite um valor: '))
c = (math.pow(a,2)+math.pow(b,2))
h = math.sqrt(c)
print('{:.2f}'.format(h))'''

#calculo hipotenusa 2
'''a = float(input('Cateto oposto: '))
b = float(input('Cateto adjacente: '))
h = ((a**2)+(b**2))**(1/2)
print(h)'''

#calcular hipotenusa 3
'''from math import hypot
a = float(input('Cateto Oposto: '))
b= float(input('Cateto Adjacente: '))
h = hypot(a, b)
print(h)'''

#leio o ângulo e mostre o seno cosseno e tangente
'''#from math import sin, cos, tan, radians
import math
num = float(input('Ângulo: '))
seno = math.sin(math.radians(num))
coss = math.cos(math.radians(num))
tang = math.tan(math.radians(num))
print('Seno: {:.2f}, Cosseno: {:.2f}, Tangente: {:.2f}'.format(seno, coss, tang))'''

# sortear um aluno entre 4 e mostrar seu nome
'''import random
n1 = str(input('Nome: '))
n2 = str(input('Nome: '))
n3 = str(input('Nome: '))
n4 = str(input('Nome: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('Escolhido: {}'.format(escolhido))'''

#mostrar uma ordem aleatoria dos alunos (todos)
import random
n1 = str(input('Nome: '))
n2 = str(input('Nome: '))
n3 = str(input('Nome: '))
lista = [n1, n2, n3]
random.shuffle(lista) #shuffle embaralha a lista
print(lista)