'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
print('\033[1;33m-=\033[m' * 20)
lnome = []
lmedia = []
lnotas = []
aux = []
cadastro = []
while True:
    nome = str(input('\033[31mDigite seu nome: \033[m')).capitalize()
    nota1 = float(input('\033[32mNota 1: \033[m'))
    nota2 = float(input('\033[33mNota 2: \033[m'))
    lnome.append(nome)
    lmedia.append((nota1 + nota2) / 2)
    lnotas.append(nota1)
    lnotas.append(nota2)
    aux.append(lnome[:])
    aux.append(lmedia[:])
    aux.append(lnotas[:])
    cadastro.append(aux[:])
    lnome.clear()
    lmedia.clear()
    lnotas.clear()
    aux.clear()
    sair = ' '
    while sair not in 'SN':
        sair = str(input('\033[34mContinuar [S/N]:\033[m ')).upper().strip()[0]
    if sair == 'N':
        break
    print('\033[1;33m-=\033[m' * 20)
print('\033[1;33m-=\033[m' * 20)
print('\033[35mNo. Nome          Média\033[m')
print('-' * 26)
for i, p in enumerate(cadastro):
    print(f'\033[36m{i}  \033[m ', end='')
    for e in p[0]:
        print(f'\033[37m{e:<10}\033[m', end='')
    for e in p[1]:
        print(f'\033[31m{e:>9}\033[m')
print('-' * 26)
while True:
    aluno = int(input('\033[32mMostrar notas de qual aluno?\033[m '))
    for i, p in enumerate(cadastro):
        if aluno == i:
            for d in p[0]:
                print(f'\033[33mAs notas de \033[m\033[36m{d}\033[m\033[33m foram \033[m', end='')
            for d in p[2]:
                print(f'\033[34m{d} \033[m', end='')
    print()
    sair = ' '
    while sair not in 'SN':
        sair = str(input('\033[35mContinuar [S/N]: \033[m')).upper().strip()[0]
    if sair == 'N':
        break
    print('\033[1;33m-=\033[m' * 20)
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
