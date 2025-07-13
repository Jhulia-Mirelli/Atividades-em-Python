import random
from random import randint
soma = venc =0
while True:
    jogador = int(input("Digite seu número: "))
    computador = random.randint(1,10)
    print(computador)
    soma = jogador + computador
    res = " "
    while res not in "PI":
        res = str(input("[I]Ímpar ou [P]Par?")).strip()[0].upper()
    print("Deu par"if soma % 2 == 0 else "Deu impar")
    if res == "I":
        if soma % 2 == 0:
            print(f"PERDEU!!\nTotal de vitórias: {venc}")
            break
        else:
            venc += 1
            print("VENCEU!!")
    elif res == "P":
        if soma % 2 == 0:
            venc += 1
            print("VENCEU!!")
        else:
            print(f"PERDEU!!\nTotal de vitórias: {venc}")
            break

