from time import sleep


def contagem(a, b, c):
    if c == 0:
        c = 1
    if c < 0:
        c = abs(c)

    print(f"Contagem de {a} até {b} de {c} em {c}")
    if a > b:
        for c in range(a, b - 1, -c):
            print(c, end=' ')
            # sleep(0.5)
        print("FIM!")

    else:
        for c in range(a, b + 1, c):
            print(c, end=' ')
            # sleep(0.5)
        print("FIM!")


contagem(1, 10, 1)
contagem(10, 0, 2)

print("Agora é sua vez de personalizar a contagem!")
n1 = int(input("Início: "))
n2 = int(input("Fim: "))
n3 = int(input("Passo: "))

contagem(n1, n2, n3)
