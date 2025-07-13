def escreva(txt):
    tam = len(txt)+4
    print("~"*tam)
    print(f"  {txt}")
    print("~"*tam)


while True:
    t = str(input("Digite seu texto: "))
    escreva(t)

    res = int(input("Deseja continuar? [1]sim [2]nao" ))
    if res == 2:
        break
