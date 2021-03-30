'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
n1 = float(input('\033[30mDigite o primeiro número:\033[m '))
n2 = float(input('\033[31mDigite o segundo número:\033[m '))
n3 = float(input('\033[32mDigite o terceiro número:\033[m '))
if n1 > n2 and n1 > n3:
    print('\033[33mMaior número\033[m {}{:.1f}{}'.format('\033[31m', n1, '\033[m'))
if n2 > n1 and n2 > n3:
    print('\033[34mMaior número\033[m {}{:.1f}{}'.format('\033[32m', n2, '\033[m'))
if n3 > n1 and n3 > n2:
    print('\033[35mMaior número\033[m {}{:.1f}{}'.format('\033[33m', n3, '\033[m'))
if n1 < n2 and n1 < n3:
    print('\033[36mMenor número\033[m {}{:.1f}{}'.format('\033[34m', n1, '\033[m'))
if n2 < n1 and n2 < n3:
    print('\033[37mMenor número\033[m {}{:.1f}{}'.format('\033[35m', n2, '\033[m'))
if n3 < n1 and n3 < n2:
    print('\033[30mMenor número\033[m {}{:.1f}{}'.format('\033[36m', n3, '\033[m'))
print('\033[33m----------\033[m')
