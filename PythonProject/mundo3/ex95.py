#melhor codigo do jogador, looping de jogaador e escolher visualizar os jogador de cada um
grupo = []
jogador = {}
gol = []
totg= cont = 0
while True:
    jogador['nome'] = str(input("Nome do Jogador: "))
    totp = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for c in range(totp):
        ngol = int(input(f"Quantos gol na partida {c+1}? ")) #numeros de gols por partida
        totg += ngol
        gol.append(ngol)
        jogador['gols'] = gol.copy()
        jogador['total'] = totg
    totg=0
    cont+=1
    grupo.append(jogador.copy())
    jogador.clear()
    gol.clear()
    res = str(input("Deseja continuar? [S]Sim [N]Não")).upper().strip()[0]
    if res not in ("S","N"):
        res = str(input("Deseja continuar? [S]Sim [N]Não")).upper().strip()[0]
    if res == "N":
        break
print("=-"*20)
print(f"{'cod':<2}",end=" ")
print(f"{'nome':<17}",end=" ")
print(f"{'gols':<17}",end=" ")
print(f"{'total':<17}",end=" ")

print()
for i, v in enumerate(grupo):
    print(f"{i:<2}",end=" ")
    for d in v.values():
        print(f"{str(d):<19}", end="")
    print()
while True:
    res2 = int(input("Mostrar dados de qual jogador? (999 sair): "))
    if res2 == 999:
        break
    if res2 >= len(grupo):
        print("ERRO!!")
    else:
        print(f"LEVANTAMENTO DO JOGADOR {grupo[res2]['nome']}")
        for i,v in enumerate(grupo[res2]['gols']):
            print(f"No jogo {i+1} fez {v} gols.")

