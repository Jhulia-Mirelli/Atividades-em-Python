#nome de cidade e se começa com santos

cidade = str(input('Digite o nome da cidade: ')).strip()#tirando os espaços do começo e fim
print(cidade.split()[0].lower() =='santos')