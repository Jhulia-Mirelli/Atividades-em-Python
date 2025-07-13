def fatorial1(n, show=False):
    '''
        Cáculo de Fatórial
    :para n: passagem de número para o cálculo do fatórial
    :para show: (opcional) mostrar a conta ou não
    :return: fatorial de n
    '''

    from math import factorial
    f = factorial(n)
    if show:
        n1 = n
        while n1 > 0:
            if n1 == 1:
                print(f"{n1}=", end="")
            else:
                print(f"{n1}x", end="")
            n1 -= 1
        return f
    else:
        return f


print(fatorial1(5, True))
#help(fatorial1)
