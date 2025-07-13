import random
num = random.randint(0,5)
print(num)
n1 = int(input("Adivinhe o número que estou pensando de 0 a 5..."))
print("Acertou" if n1 == num else "Errou!!")