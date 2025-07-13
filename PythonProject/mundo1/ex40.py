#nota media final
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = float((n1+n2)/2)
if media >= 7:
    print("\033[32mAPROVADO!!\033[m\nMédia: {:.1f}".format(media))
elif media <= 5:
    print("\033[31mREPROVADO!!\033[m\nMédia: {:.1f}".format(media))
else:
    print("\033[33mRECUPERAÇÃO!!\033[m\nMédia: {:.1f}".format(media))