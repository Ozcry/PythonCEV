'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
PARES sorteados pela função anterior.'''
from random import randint
from time import sleep


def sorteia(num):
    print('\033[1;33m-=\033[m' * 20)
    print('\033[34mSorteando 5 valores da lista: \033[m', end='')
    for c in range(0, 5):
        b = int(randint(0, 9))
        num.append(b)
        print(b, end=' ')
        sleep(0.5)
    print('\033[1;32mPRONTO!\033[m')


def somapar(num):
    soma = 0
    for c in num:
        if c % 2 == 0:
            soma += c
    print(f'\033[35mSomando os valores pares de\033[m {num}\033[35m, temos \033[m{soma}')
    print('\033[1;33m-=\033[m' * 20)
    print('\033[1;32mFIM\033[m')


lst = []
sorteia(lst)
somapar(lst)
