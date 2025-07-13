km_dis = float(input("Qual a distância da viagem em Km? "))
passagem = 0
if km_dis <= 200.0:
    passagem = km_dis * 0.50
else:
    passagem = km_dis * 0.45
print("Valor da passagem: R$ {:.2f}".format(passagem))

