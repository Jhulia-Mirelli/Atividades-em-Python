#adivinha o numero q o pc pensa
from random import randint
from time import sleep
computador = randint(1,10)
jogador = ""
cont = 1
print(computador)
jogador = int(input("Adivinhe em que número estou pensando..."))
while jogador != computador:
    jogador = int(input("\033[31mERROU\033[m\nTente novamente..."))
    cont += 1
print("PARABÉS!!\nVocê acertou na {}° tentativa".format(cont))