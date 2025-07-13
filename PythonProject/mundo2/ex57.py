#leia somente sexo f e m e se digitar errado peça novamente
sexo = ''
while sexo != 'A' and sexo != 'B':
    sexo = str(input("Digite [A] ou [B]: ")).upper()[0].strip()
    if sexo != 'A' and sexo != 'B': #while sexo not in 'AaBb':
        print("\033[31mEssa opção é inválido\033[m\nDigite novamente!!")