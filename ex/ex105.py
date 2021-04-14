'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
A) Quantidade de notas
B) A maior nota
C) A menor nota
D) A média da turma
E) A situação (opcional)
Adicione também as Docstrings da função.'''


def notas(*num, sit=False):
    """==> Função para analisr notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adcionar a situação
    :return: dicionário com várias informações sobre a situação da turma"""
    print('\033[1;33m-=\033[m' * 20)
    turma = {}
    maior = menor = soma = cont = 0
    for c in num:
        soma += c
        if cont == 0:
            maior = menor = c
        if c > maior:
            maior = c
        elif c < menor:
            menor = c
        cont += 1
    media = soma / cont
    turma['total'] = cont
    turma['maior'] = maior
    turma['menor'] = menor
    turma['media'] = media
    if sit:
        if media >= 7:
            turma['situação'] = 'Boa'
        elif 5 <= media < 7:
            turma['situação'] = 'Razoavel'
        else:
            turma['situação'] = 'Ruim'
    return turma


print(notas(5.5, 9.5, 10, 6.5, sit=True))
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
