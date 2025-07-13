#ler nome do produto e preço, total gasto, produtos acima de 1000 nome do produto mais barato
totpreco = totprod1000 = menor = cont = 0
menorproduto = ""
while True:
    nomproduto = str(input("Digite o nome do produto: ")).strip().upper()
    preco = float(input("Qual o preço do produto? "))
    totpreco +=preco
    cont+=1

    if preco > 1000:
        totprod1000 += 1

    if cont == 1 or preco <= menor:
            menor = preco
            menorproduto = nomproduto
    res = " "
    while res not in "SN":
        res = str(input("Deseja continuar?")).strip()[0].upper()
    print("-"*30)

    if res != "S":
        break

print(f"Total gasto R$ {totpreco}\n{totprod1000} Produtos acima de R$ 1000,00\n{menorproduto} é o produto mais barato custando R$ {menor}")
