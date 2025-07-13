# pedra papel e tesoura
import random

computador = random.randint(1, 3)
print(computador)
resposta = int(input("Vamos jogar Jokenpô? [1]Sim [2]Não "))
if resposta == 1:
    print("-" * 20)
    jogador = int(input("Escolha:\n[1]Pedra\n[2]Papel\n[3]Tesoura\n"))
    if computador == jogador:
        print("{} X {}\nEmpate".format(computador, jogador))
    if computador != jogador:
        if computador == 1 and jogador == 2:
            print("Perdi!!\n{} vence {}".format(jogador, computador))
        elif computador == 2 and jogador == 1:
            print("VENCI!!\n{} vence {}".format(computador, jogador))
        elif computador == 3 and jogador == 2:
            print("VENCI!!\n{} vence {}".format(computador, jogador))
        elif computador == 2 and jogador == 3:
            print("Perdi!!\n{} vence {}".format(jogador, computador))
        elif computador == 1 and jogador == 3:
            print("VENCI!!\n{} vence {}".format(computador, jogador))
        elif computador == 3 and jogador == 1:
            print("Perdi!!\n{} vence {}".format(jogador, computador))
else:
    print("Ok, talvez mais tarde!!")
