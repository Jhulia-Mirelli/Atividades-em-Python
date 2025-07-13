lista =(int(input("Digite um valor: ")),int(input("Digite um valor: ")),
        int(input("Digite um valor: ")),int(input("Digite um valor: ")))
print(lista)
print(f"O valor 9 apareceu {lista.count(9)}x")
if 3 in lista:
    print(f"O primeiro valor 3 foi digitado na posição {lista.index(3)+1}")
else:
    print("Nenhum valor 3 registrado")
print(f"Valor par registrado: ",end="")
for n in lista:
    if n % 2 ==0:
        print(n,end=" ")
    else:
        print(f"Nenhum valor par registrado")
        break