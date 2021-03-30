'''Desenvolva um programa que leia o primeiro termo e a razão de um PA. no final, mostre os 10 primeiros termos dessa
progressão.'''
print('\033[1;33m-=\033[m' * 20)
n1 = int(input('\033[31mDigite o primeiro termo:\033[m '))
pa = int(input('\033[32mDigite a razão da PA:\033[m '))
print('\033[34mOs Próximos 10 termos da sua PA são:\033[m')
for c in range(n1 + pa, n1 + pa * 11, pa):
    print('{} '.format(c), end='')
print('\033[35mFIM\033[m')
print('\033[1;33m-=\033[m' * 20)
