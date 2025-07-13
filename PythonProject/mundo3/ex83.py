#input de expressão matematica e confirmar se os parentes estão certos
contp = 0
exp = str(input("Digite uma expressão matemática: "))
if "(" in exp:
    print("Aberto parenteses,",exp.count("("))
    if ")" in exp:
        print("Fechado",exp.count(")"))
        if exp.count("(") != exp.count(")"):
            print("Expressão errada!")
        else:
            print("Expressão certa!")
