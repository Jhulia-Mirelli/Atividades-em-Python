#unidade centena dezena milhar
num = int(input('Digite um valor: '))
#print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num[3],num[2],num[1],num[0])) dessa forma da erro
u = num//1%10
d = num//10%10
c = num//100%10
m = num//1000%10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u,d,c,m))