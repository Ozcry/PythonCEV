'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint
maior = menor = 0
cinco = randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)
if cinco[0]:
    maior = cinco[0]
    menor = cinco[0]
for c in cinco:
    if c > maior:
        maior = c
    elif c < menor:
        menor = c
print('\033[1;33m-=\033[m' * 20)
print('\033[34mOs valores sorteados foram\033[m ', end='')
for c in cinco:
    print(c, end=' ')
print(f'\n\033[35mO menor valor sorteado foi \033[m{menor}')
print(f'\033[36mO maior valor sorteado foi \033[m{maior}')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
