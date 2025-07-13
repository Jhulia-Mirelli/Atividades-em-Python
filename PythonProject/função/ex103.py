# ficha de jogador
def ficha(n='', g=''):
    if n == "":
        return f"O jogador <desconhecido> fez {g} gol(s) no campeonato."
    elif g == 0 or g.isnumeric()==False:
        return f"O jogador {n} fez {0} gol(s) no campeonato."
    else:
        return f"O jogador {n} fez {g} gol(s) no campeonato. "


nome = str(input("Nome do Jogador: ")).strip()
gol = input("Quantos gols foram marcados?")
if gol == '':
    gol = 0
print(ficha(nome, gol))
