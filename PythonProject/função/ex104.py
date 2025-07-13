def leiaInt(num):
    num = input(num)
    n = num.isnumeric()
    if n:
        return num
    else:
        while n == False:
            print(f"\033[31mERRO!Digite um número inteiro válido.\033[m")
            num = input("Digite um número: ")
            n = num.isnumeric()
    return num


num = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {num}")
