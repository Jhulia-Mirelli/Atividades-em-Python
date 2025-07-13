''''# leia número inteiro e mostre o sucessor e o antecessor
n = int(input('Digite um valor: '))
print('{}-{}-{}'.format((n-1),n,(n+1)))'''

''''# mostrar o dobro, o triplo e a raiz quadrada
n = int(input('Digite um valor: '))
print('{}-{}-{:.2f}'.format((n*2),(n*3),(n**(1/2)))) #pow(n, (1/2)) função para raiz quadrada'''

'''#nota do aluno e sua média
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float (input('Digite a terceira nota: '))
media = (n1+n2+n3)/3
print('Média do aluno: {:.1f}'.format(media))'''

'''#metros convertido em centimetros e milímetros
n = float(input('Digite um valor: '))
print('Seu valor em metro é {} em centímetro é {:.0f} e em milímetro é {:.0f}'.format(n,n*100,n*1000))'''

'''#tabuada
n = int(input('Digite um valor: '))
print('tabuada do número {}'.format(n))
print('{} x {}= {}'.format(n,1,n*1))
print('{} x {}= {}'.format(n,2,n*2))
print('{} x {}= {}'.format(n,3,n*3))
print('{} x {}= {}'.format(n,4,n*4))
print('{} x {}= {}'.format(n,5,n*5))
print('{} x {}= {}'.format(n,6,n*6))
print('{} x {}= {}'.format(n,7,n*7))
print('{} x {}= {}'.format(n,8,n*8))
print('{} x {}= {}'.format(n,9,n*9))
print('{} x {}= {}'.format(n,10,n*10))'''

'''#solicitar um valor em dinheiro e mostrar quanto ela teria em dolares 1=3,27
valor = int(input('Digite um valor: '))
print('valor convertido em dolars: {}'.format(valor * 5.81))'''

'''#calcular area
l = float(input('Digite um valor: '))
c = float(input('Digite um valor: '))
print('Área total: {}'.format(l*c))
tinta = (l*c)/2
print('Tinta necessária {}L'.format(tinta))'''

'''#preço com desconto de 5%
valor = int(input('Digite o valor: '))
print('valor com desconto de 5%: R$ {}'.format(valor - (valor * (5/100))))

#salario com aumento
salario =  int(input('Digite seu sálario: '))
print('Seu sálario com ajuste de 15%: R$ {}'.format((salario + (salario * (15/100)))))'''

#conversor de temperatura
'''t = float(input('Qual a temperatura? °C '))
f = (t*1.8)+32
print('Temperatura em °F {:.1f}'.format(f))'''

#programa de carro de aluguel
km = float(input('Quantos km percorridos?'))
dias = int(input('Quantos dias?'))
valor_total = (60 * dias) + (0.15*km)
print('Valor total a pagar: R$ {:.2f}'.format(valor_total))


