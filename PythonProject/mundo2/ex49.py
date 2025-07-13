#tabuada
n = int(input("A tabuada de qual número você gostaria de ver?"))
print(f"{'TABUADA DO {}':=^40}".format(n))
for c in range(1,11):
    print("{:2} X {:2} = {:2}".format(n,c,c*n))