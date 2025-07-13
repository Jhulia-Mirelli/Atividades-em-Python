#soma total do números impares entre 1 à 500
total = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont += 1
        total += c
        print(c,end = " ")
print("\ntotal de todos os {} é: {}".format(cont,total))