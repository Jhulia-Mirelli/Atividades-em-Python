def aumentar(v=0, a=10, f=True):#parametros com valores para não dar problema se não for passado valor nenhum na chamada
    v = v + (v * (a / 100))
    return v if f is False else formatação(v)


def diminuir(v=0, d=5, f=True):
    v = v - (v * (d / 100))
    return v if f is False else formatação(v)


def dobro(v=0, f=True):
    v *= 2
    return v if f is False else formatação(v)


def metade(v=0, f=True):
    v = v // 2
    return v if f is False else formatação(v)


def formatação(v=0):
    return f"R${v:>.2f}".replace('.', ',')


def resumo(v=0, a=10, d=5):
    print("-" * 30)
    print("  RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{formatação(v)}")
    print(f"Dobro do preço: \t{dobro(v)}")
    print(f"Metade do preço: \t{metade(v)}")
    print(f"{a}% de aumento: \t{aumentar(v,a)}")
    print(f"{d}% de redução: \t{diminuir(v,d)}")#posso estacar essa tabulção\t\t
    print("-" * 30)
