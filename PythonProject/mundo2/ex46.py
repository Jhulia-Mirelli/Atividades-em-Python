#contagem regressiva fogos tempo de espera
from time import sleep
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print("\033[31mBUMMM\033[m")