def leiaDinheiro(msg):
    valido = False
    while not valido:
        v = str(input(msg)).replace(',', '.').strip()
        if v.isalpha() or v == "":
            print(f"\033[31mERRO! {v} é um preço inválido\033[m")
        else:
            valido = True
            return float(v)
    return None
