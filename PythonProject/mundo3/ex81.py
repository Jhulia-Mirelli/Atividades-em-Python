lista = []
cont = 0
while True:
    n = int(input("Digite um valor:"))
    lista.append(n)
    res = str(input("Deseja continuar? [S]Sim [N]Não ")).upper().strip()[0]
    while res not in "SN":
        res = str(input("Deseja continuar? [S]Sim [N]Não ")).upper().strip()[0]
    cont += 1
    lista.sort(reverse=True)
    if res == "N":
        print(f"Lista reversa: {lista}")
        print(f"{cont} valores registrados")
        if 5 in lista:
            print("Valor 5 registrado!")
        else:
            print("Valor 5 não foi registrado.")
        break