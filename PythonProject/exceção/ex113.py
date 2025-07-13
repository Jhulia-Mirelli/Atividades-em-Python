def leiaInt(num):
    try:
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
    except KeyboardInterrupt:
        print("\033[31mO usuário preferiu não digitar um valor\033[m")
        return 0


def leiaFloat(num):
    try:
        num = str(input(num)).replace(',','.').strip()
        valido = num.isalpha()
        if not valido and num != "":
            return float(num)
        else:
            while valido or num == "":
                print(f"\033[31mERRO!Digite um número real válido.\033[m")
                num = str(input("Digite um valor real: ")).replace(',','.').strip()
                valido = num.isalpha()
            return float(num)
    except KeyboardInterrupt:
        print("\033[31mO usuário preferiu não digitar um valor\033[m")
        return 0


num1 = leiaInt("Digite um valor inteiro: ")
num2 = leiaFloat("Digite um valor real: ")
print(f"Você acabou de digitar o valor inteiro {num1} e o valor real {num2}")
