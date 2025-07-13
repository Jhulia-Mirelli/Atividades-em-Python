from time import sleep


def maior(*num):
    maior1 = tot= 0
    print("-=" * 30)
    print("Analisando os valores...")
    sleep(1)
    for n in num:
        if tot == 0:
            maior1 = n
        else:
            if n >= maior1:
                maior1 = n
        tot += 1
        print(f"{n}", end=" ")
    print(f"Foram informados {len(num)} valores no total.")
    print(f"O maior valor foi {maior1}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
