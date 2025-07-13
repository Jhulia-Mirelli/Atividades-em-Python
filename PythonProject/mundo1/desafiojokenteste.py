from random import randint
itens = ("pedra","papel","tesoura")
computador = randint(0,2)
print("O computador escolheu {}".format(itens[computador]))