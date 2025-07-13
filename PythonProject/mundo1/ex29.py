km = float(input("Velocidade Km: "))
if km > 80.0:
    multa = ((km-80) * 7)
    print("Você foi multado em R$ {:.2f}\nSua velocidade estava acima do limite".format(multa))