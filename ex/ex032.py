'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.'''
from datetime import date
a = int(input('\033[36mDigite um ano:\033[m '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('\033[32mSeu ano e Bissexto!\033[m')
    print('\033[33m-----------\033[m')
else:
    print('\033[31mNão e Bissexto!\033[m')
    print('\033[33m-----------\033[m')
