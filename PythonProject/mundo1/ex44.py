# pagamento produto
print(f"{' LOJA ':=^40}")
valor = float(input("Valor do produto: R$ "))
print("-" * 20 + "\nForma de Pagamento\n" + "-" * 20)
resposta = int(input('''Digite:
[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2X no cartão
[4] 3X ou mais no cartão com 20% de juros))\n'''))
print("-" * 20)
if resposta == 1:
    valortotal = valor - (valor * (10 / 100))
    print("Valor do produto: R$ {:.2f}\nTotal a pagar: R$ {:.2f}".format(valor, valortotal))
elif resposta == 2:
    valortotal = valor - (valor * (5 / 100))
    print("Valor do produto: R$ {:.2f}\nTotal a pagar: R$ {:.2f}".format(valor, valortotal))
elif resposta == 3:
    valorparc = valor / 2
    print("Valor do produto: R$ {:.2f}\n"
          "Sua compra sera parcelada em 2X de R$ {:.2f} sem juros".format(valor, valorparc))
elif resposta == 4:
    parcelas = int(input("Quantas parcelas? "))
    print("-" * 20)
    valortotal = valor + (valor * (20 / 100))
    valorparc = valortotal / parcelas
    print("Valor do produto: R$ {:.2f}\nValor a pagar: R$ {:.2f}\n"
          "Sua compra sera parcelada em {}X de R$ {:.2f} com juros".format(valor, valortotal, parcelas, valorparc))
else:
    print("\033[31mOpção Inválida\033[m")
