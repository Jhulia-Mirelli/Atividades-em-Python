#pa
p1 = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
cont = 10
res = 1
total = 0
while res != 0:
    while cont != 0:
        print(p1,end=" ")
        p1 += razão
        cont -= 1
        total += 1
    res = int(input("\nQuantos termos você gostaria de mostar a mais?"))
    if res !=0:
        cont = res

print("Ao todo foram mostrados {} termos".format(total))

