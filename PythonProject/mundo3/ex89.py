lista = []
while True:
    aluno = [[input("Digite o nome: ")],[float(input("Digite 1° nota: ")),float(input("Digite 2° nota: "))]]
    lista.append(aluno[:])
    aluno.clear()

    res = str(input("Deseja continuar? [S]Sim [N]Não: ")).upper().strip()[0]
    while res not in "SN":
        print("\033[31mOpção inválida!\033[m")
        res = str(input("Deseja continuar? [S]Sim [N]Não: ")).upper().strip()[0]
    if res =="N":
        break
nota=nota1= nota2 = media=0
print("-"*30)
print("N° | Nome     | Média")
for i,a in enumerate(lista):
    nota = a[1]
    nota1 = nota[0]
    nota2 = nota[1]
    media = (nota1 + nota2) / 2
    aluno = a[0]
    print(f"{i:<4}{aluno[0]:<10}{media:>4.1f}")
while True:
    res2 = int(input("Mostrar as notas de qual aluno? (999 interrompe): "))
    if len(lista)-1 >= res2:
        print(f"Notas de {lista[res2][0]} são: {lista[res2][1]}")
    if res2 == 999:
        break