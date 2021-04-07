'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
print('\033[1;33m-=\033[m' * 20)

while True:
    nome = str(input('Digite seu nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))


    sair = ' '
    while sair not in 'SN':
        sair = str(input('Continuar [S/N]: ')).upper().strip()[0]
    if sair == 'N':
        break

print('\033[1;33m-=\033[m' * 20)
print('No. Nome          Média')
print('-' * 26)


print('\033[1;33m-=\033[m' * 20)
