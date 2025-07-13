#calculadora de 2 valores
from time import sleep
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
resposta = ''
while resposta != 5:
    resposta = int(input(('''---------------------
Escolha:
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos Números
[5]Sair do programa
---------------------\n''')))
    if resposta == 1:
        print("{}+{}={}".format(n1,n2,n1+n2))
    elif resposta == 2:
        print("{}-{}={}".format(n1,n2,n1-n2))
    elif resposta == 3:
       if n1 > n2:
           print("{} é maior que {}".format(n1,n2))
       elif n2 > n1:
           print("{} é maior que {}".format(n2,n1))
       else:
           print("Os dois valores são iguais")
    elif resposta == 4:
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite um valor: "))
    elif resposta == 5:
        print("Finalizando", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print("\nVolte Sempre!")
        resposta = 5
    else:
        print("\033[31mOpção inválida!!\033[m")