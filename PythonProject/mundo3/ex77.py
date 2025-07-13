#tupla com várias palavras print vogais de cada palavra
lista = ('Zero', 'm', 'Doiso', 'Tres', 'Quatroo', 'amarelo')
a = e = i = o = u = 0
for palavra in lista:
    print(f"\nNa palavra {palavra.upper()} temos ", end="")
    if "a" in palavra.lower():
        a = palavra.count("a")
    print("a " * a, end="")
    if "e" in palavra:
        e = palavra.count("e")
        print("e " * e, end="")
    if "i" in palavra:
        i = palavra.count("i")
        print("i " * i, end="")
    if "o" in palavra:
        o = palavra.count("o")
        print("o " * o, end="")
    if "u" in palavra.lower():
        u = palavra.count("u")
        print("u " * u, end="")
