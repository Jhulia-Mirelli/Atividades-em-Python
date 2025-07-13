from ex115refeito.lib.interface import *
from ex115refeito.lib.arquivo import *
from time import sleep

# criação de arquivo para salvar listagem de pessoas
arq = "cursoemvideo.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    res = menu(["Listar Pessoas", "Cadastrar Pessoas ", "Sair do Sistema"])
    if res == 1:
        lerArquivo(arq)
    elif res == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome:")).strip()
        idade = leiaInt("Idade:")
        cadastro(arq, nome, idade)
    elif res == 3:
        cabecalho("Saindo do Sistema...Até Logo!")
        break
    else:
        print("\033[31mErro! Digite uma opção válida\033[m")
        sleep(1)
