import requests


def validar(url):
    try:
        res = requests.get(url)
        print(res.status_code)
        if res.status_code == 200:
            return print("\033[32mConsegui acessar o site Pudim com sucesso!\033[m")
    except Exception:
        return print("\033[31mNão foi possivel acessar o site Pudim :(\033[m")


validar("https://pudim.com/")
