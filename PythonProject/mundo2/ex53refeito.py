frase = str(input("Digite sua frase: ")).strip().lower()
juntar = frase.split()
frase_sem_espaco = "".join(juntar)
inverso = ""

for letra in range (len(frase_sem_espaco)-1,-1,-1): #len -1 pq começa a contar no 0,
                                                    # -1 pq precisamos ir até o zero senao ele desconsidera e
                                                    # -1, há menos um passo
    inverso += frase_sem_espaco[letra]

if inverso == frase_sem_espaco:
    print("Essa frase é um palíndromo")
else:
    print("frase normal")

print(inverso, frase_sem_espaco)

