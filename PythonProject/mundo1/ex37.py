#converter em binario ou octal ou hexadecimal
n = int(input("Digite um valor: "))
escolha = int(input("Escolha em que base deseja converter:\n[1]Binário\n[2]Octal\n[3]Hexadecimal\nSua opção: "))
if escolha == 1:
    print("Valor {} convertido para Binário: {}".format(n,bin(n)[2:]))
elif escolha == 2:
    print("Valor {} convertido para Octal: {}".format(n,oct(n)[2:]))
elif escolha == 3:
    print("Valor {} convertido para Hexadecimal : {}".format(n,hex(n)[2:]))
else:
    print("\033[31mnúmero inválido\033[m")