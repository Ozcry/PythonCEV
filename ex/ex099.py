'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''


def maior(*num):
    m = 0
    me = 0
    for c in num:
        if m == 0 and me == 0 and c == num[0]:
            m = c
            me = c
        if c < me:
            me = c
        if c > m:
            m = c
    print('\033[1;33m-=\033[m' * 20)
    print(f'\033[34mVocê digitou \033[m{num} \n\033[35mMaior valor\033[m {m} \n\033[36mMenor valor\033[m {me}')
    print('\033[1;33m-=\033[m' * 20)
    print('\033[1;32mFIM\033[m')


maior(1, 2, 3, 4, 5, 6, 7, 8, 9)
maior(3, 7, 44, 3, 5, 7, 9, 3)
maior(9, 3, 99, 32, 45, 76, 4)
maior(0, 1, 9)
maior(0, 1, 0, 2)
maior()
