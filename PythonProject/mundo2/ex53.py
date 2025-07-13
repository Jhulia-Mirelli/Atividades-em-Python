#ler uma frase e dizer se é um palindromo ex: apos a sopa<< pode ser lida nas duas direçoes desconsiderar espaços
frase = str(input("Digite sua frase: ")).lower().strip()
frase = frase.replace(" ","")
inverte = frase[::-1]
if frase == inverte:
    print("Essa é uma frase palíndrma!!")
else:
    print("Essa é uma frase normal")
print(frase,inverte)