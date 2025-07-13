import random

lista = ["pedra", "papel", "tesoura"]
aleatorio = random.choice(lista)
resposta = int(input("Vamos jogar Jokenpô? [1]Sim [2]Não "))
if resposta == 1:
    print("-" * 20)
    jogador = str(input("Escolha:\nPedra\nPapel\nTesoura\n")).lower()
    print("-"*20)
    print("O computador jogou \033[4m{}\033[0m".format(aleatorio))
    if aleatorio == jogador:
        print("EMPATE\n{} X {}".format(aleatorio, jogador))
    if aleatorio != jogador:
        if aleatorio == "pedra" and jogador == "papel":
            print("\033[32mVENCEU!!!!\033[m\n{} vence {}".format(jogador, aleatorio))
        elif aleatorio == "papel" and jogador == "pedra":
            print("\033[31mPERDEU!!\033[m\n{} vence {}".format(aleatorio, jogador))
        elif aleatorio == "tesoura" and jogador == "papel":
            print("\033[31mPERDEU!!\033[m\n{} vence {}".format(aleatorio, jogador))
        elif aleatorio == "papel" and jogador == "tesoura":
            print("\033[32mVENCEU!!!!\033[m\n{} vence {}".format(jogador, aleatorio))
        elif aleatorio == "pedra" and jogador == "tesoura":
            print("\033[31mPERDEU!!\033[m\n{} vence {}".format(aleatorio, jogador))
        elif aleatorio == "tesoura" and jogador == "pedra":
            print("\033[32mVENCEU!!!!\033[m\n{} vence {}".format(jogador, aleatorio))
        else:
            print("\033[31mVocê Jogou uma Opção Inválida\033[m")
else:
    print("OK, talvez mais tarde!!")
