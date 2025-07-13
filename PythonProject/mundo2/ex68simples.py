#jogo de par ou impar
import random
n = ["par","impar"]
while True:
    computador = random.choice(n)
    print(computador)
    print("-"*30)
    print("Vamos jogar? Escolha:")
    jogador = str(input("Par ou Ímpar: ")).strip().lower()
    print("-" * 30)
    if computador == "impar" and jogador == "par":
        print(f"VENCEU!\nEu joguei {computador} e você jogou {jogador}")
    elif computador == "par" and jogador == "impar":
        print(f"PERDEU!!\nEu joguei {computador} e você jogou {jogador}")
        break
    else:
        print(f"EMPATOU!!\nEu joguei {computador} e você jogou {jogador}")
