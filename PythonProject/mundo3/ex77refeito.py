lista = ('Zero', 'm', 'Doiso', 'Tres', 'Quatroo', 'amarelo')

for palavra in lista:
    print(f"\nNa palavra {palavra.upper()} temos:", end=" ")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra, end=" ")