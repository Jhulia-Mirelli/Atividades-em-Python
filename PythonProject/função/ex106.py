cores = {0: '\033[m',  # nada
         1: '\033[::42m',  # verde
         2: '\033[::44m',  # azul
         3: '\033[::47m',  # branco
         4: '\033[::41m'}  # vermelho

def ajuda(txt):
    titulo(f"Acessando manual do comando '{txt}'", 2)
    print(cores[3],end="")
    print(help(txt))
    print(cores[0], end="")

def titulo(txt, cor=0):
    print(cores[cor],end="")
    print("~" * (len(txt) + 4))
    print(f"  {txt}")
    print("~" * (len(txt) + 4))
    print(cores[0],end="")

def comando():
    res = ''
    while True:
        titulo("SISTEMA DE AJUDA PyHELP",1)
        res = input("Função ou Biblioteca > ").upper()
        if res.upper() == 'FIM':
            break
        else:
            ajuda(res.lower())
    titulo("ATÉ LOGO",4)


r = comando()
