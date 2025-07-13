#pa infinita
resposta = int(input("Deseja iniciar o programa? [1]SIM [1]NÃO\n"))
while resposta == 1:
    p1 = int(input("Digite o primeiro termo: "))
    razao = int(input("Digite a razão: "))
    print(p1, end=" ")
    for c in range(1,10):
        p1 +=razao
        print(p1, end=" ")
    resposta = int(input("\nDeseja continuar? [1]SIM [2]NÃO\n"))