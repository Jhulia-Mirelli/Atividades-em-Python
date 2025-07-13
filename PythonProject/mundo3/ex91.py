#Jogo de dados, 4 jagadas, mostrar ranking
from operator import index
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1':randint(1,6),'Jogador2':randint(1,6),
        'Jogador3':randint(1,6),'Jogador4':randint(1,6)}
print("Valores sorteados:")
for i, j in jogo.items():
    print(f" O {i} tirou {j}")
    #sleep(1)
ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1),reverse=True)
for i, j in enumerate(ranking):
    print(f"{i+1}° lugar: {j[0]} com {j[1]}")

