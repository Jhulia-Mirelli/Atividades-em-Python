def cadastro(opcao):
    temporario = dict()
    while True:
        try:
            if opcao == 3:
                break

            elif opcao == 1:
                for c,p in enumerate(lista):
                    print(c,p)
                return menu()
            elif opcao == 2:
                temporario.clear()
                nome = str(input("Nome: ")).strip()
                idade = int(input("Idade: "))
                temporario = {'nome':nome,'idade':idade}
                lista.append(temporario.copy())
                print(lista)
                return menu()


        except KeyboardInterrupt:
            return print("\n\033[31mInterrupção Forçada\033[m")
        except (ValueError, TypeError):
            print("\033[31mERRO\033[m")
            return menu()


def menu():
    try:
        print("-" * 50)
        print("MENU PRINCIPAL".center(50))
        print("-" * 50)
        print('''1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sitema''')
        print("-" * 50)
        opcao = int(input("Sua Opção: "))
        print("-" * 50)
        if opcao == 1:
            print("-" * 50)
            print("Opção 1".center(50))
            print("-" * 50)
        if opcao == 2:
            print("-" * 50)
            print("Opção 2".center(50))
            print("-" * 50)
        if opcao == 3:
            print("-" * 50)
            print("Saindo do Sistema...Até Logo!")
            print("-" * 50)
        return cadastro(opcao)

    except KeyboardInterrupt:
        return print("\n\033[31mInterrupção Forçada\033[m")
    except (ValueError, TypeError):
        print("\033[31mERRO\033[m")
        return menu()

#principal
lista = []
print(menu())
