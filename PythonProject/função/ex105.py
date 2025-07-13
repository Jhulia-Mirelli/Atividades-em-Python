def notas(*n, sit=False):
    '''
    :param n: passa as notas do aluno (aceita várias)
    :param sit: (situação) valor opcional, indicando se quer ver ou ocultar a situação
    :return: retorna dicionário com média, total de notas, maior e menor nota e situação
    '''

    turma = {}
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    media = sum(n) / len(n)
    turma['media'] = f"{media:.1f}"
    if sit:
        if media >= 7:
            turma['situação'] = 'Ótimo'
        elif media <= 6:
            turma['situação'] = 'Péssimo'
        else:
            turma['situação'] = 'Regular'
    return turma


resp = notas(3.5, 6.5, sit=True)
print(resp)
#help(notas)