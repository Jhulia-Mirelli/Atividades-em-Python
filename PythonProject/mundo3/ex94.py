#regista n pessoas, total, media de idade, nome mulheres, homem e mulher mais velhos
pessoas = []
dados = {}
tot=0
while True:
    dados['nome'] = str(input("Nome: "))
    dados['sexo'] = str(input("Sexo: [M/F]")).strip()[0].upper()
    while dados['sexo'] != "M" and dados['sexo'] != "F":
        print("ERRO! Por favor, digite apenas M ou F")
        dados['sexo'] = str(input("Sexo: [M/F]")).strip()[0].upper()
    dados['idade'] = int(input("Idade: "))
    tot += dados['idade']
    pessoas.append(dados.copy())
    dados.clear()
    res = str(input("Deseja continuar? [S]Sim [N]Não ")).upper().strip()[0]
    while res != "S" and res != "N":
        print("ERRO! Por favor, digite apenas Sim ou Não")
        res = str(input("Deseja continuar? [S]Sim [N]Não ")).upper().strip()[0]
    if res == "N":
        break
print(pessoas)
print(f"O grupo tem {len(pessoas)}")
media = tot/len(pessoas)
print(f"A média de idade é de {media:.2f} anos")
print(f"Mulheres cadastradas:", end=" ")
for c in pessoas:
    if c['sexo'] == "F":
        print(f"[{c['nome']}]",end=" ")
print("\nLista de pessoas acima da média de idade:")
for c in pessoas:
    if c['idade'] >= media:
        print("-"*10)
        for i, v in c.items():
            print(f"{i} = {v}")
print("<<ENCERRADO>>")