'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
r1 = float(input('\033[34mDigite o tamanho da primeira reta:\033[m '))
r2 = float(input('\033[35mDigite o tamanho da segunda reta:\033[m '))
r3 = float(input('\033[36mDigite o tamanho da terceira reta:\033[m '))
if r1 < r2 + r3 and r1 > r2 - r3 and r2 < r1 + r3 and r2 > r1 - r3 and r3 < r1 + r2 and r3 > r1 - r2:
    print('\033[32mPode ser um triângulo!\033[m')
    print('\033[33m-----------\033[m')
else:
    print('\033[31mNão pode ser um triângulo!\033[m')
    print('\033[33m-----------\033[m')
