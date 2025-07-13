#aproveitamento do jogaodor
jogador = {}
gol = []
jogador['nome'] = str(input('Nome do Jogador: '))
np = int(input(f"Quantas partidas {jogador['nome']} jogadou? "))
for c in range(np):
    gol.append(int(input(f"Quantos gols da {c+1} partida? ")))
jogador['gols'] = gol[:]
jogador['total'] = sum(jogador['gols'])
print()
print(jogador)
print()
for c,j in jogador.items():
    print(f"O campo {c} tem o valor {j}.")
print()
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")
for c in range(np):
    print(f"Na partida {c+1}, fez {jogador['gols'][c]} gols.")
print(f"Total de {jogador['total']} gols.")