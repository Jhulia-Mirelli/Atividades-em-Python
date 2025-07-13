a = 3
b = 5
cores ={'limpa': '\033[m',
        'azul': '\033[34m',
        'amarelo': '\033[33m',
        'pretoebranco': '\033[7m'}
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))
print('valor a igual {}{}{}'.format('\033[4;34m', a ,'\033[m'))
print('valor igual a {}{}{}'.format(cores['pretoebranco'],a, cores['limpa']))