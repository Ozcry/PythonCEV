'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a
contagem. Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada'''
from time import sleep


def contador(a, b, e):
    print('\033[1;33m-=\033[m' * 20)
    if e < 0:
        ee = e * -1
    elif e > 0:
        ee = e
    else:
        ee = 1
    print(f'\033[31mContagem de {a} até {b} de {ee} em {ee}\033[m')
    if a < b and e < 0:
        e *= -1
    if e == 0:
        e += 1
    if b < a and e > 0:
        e *= -1
    if b < a:
        for d in range(a, b - 1, e):
            print(f'\033[36m{d}\033[m', end=' ')
            sleep(0.25)
    elif b > a:
        for d in range(a, b + 1, e):
            print(f'\033[36m{d}\033[m', end=' ')
            sleep(0.25)
    print('\033[1;32mPRONTO!\033[m')
    print('\033[1;33m-=\033[m' * 20)
    print('\033[1;32mFIM!\033[m')


contador(1, 10, 1)
contador(10, 0, 2)
print('\033[1;33m-=\033[m' * 20)
print('\033[34mAgora é sua vez de personalizar a contagem!\033[m')
contador(int(input('\033[37mInício:\033[m ')), int(input('\033[35mFim:\033[m ')), int(input('\033[33mPasso:\033[m ')))
