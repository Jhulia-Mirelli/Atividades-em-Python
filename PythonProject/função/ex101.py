# programa que retorna se uma pessoa pode votar ou não
def voto(a):
    from datetime import date #Economiza memoria
    id = date.today().year - a
    if id < 16:
        msg = f"Você tem {id} anos. Voto Negado!"
    elif 16 <= id < 18 or id > 65:
        msg = f"Você tem {id} anos. Voto Opcional!"
    else:
         msg = f"Você tem {id} anos. Voto Obrigatório!"
    return msg


anonasc = int(input("Digite o ano de seu nascimento: "))
print(voto(anonasc))
