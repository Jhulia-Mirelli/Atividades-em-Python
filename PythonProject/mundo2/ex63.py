#sequencia de fibonacci
c = int(input("Deseja ver quantos termos da sequência de Fibonacci?"))
n1=0
n2=1
proximo = 0
lista = [n1,n2]
while (c-2) > 0:
    proximo = n1 + n2
    n1 = n2
    n2 =proximo
    lista.append(proximo)
    c-=1
print(lista)