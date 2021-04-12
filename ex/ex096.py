'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.'''


def area(a, b):
    m = a * b
    print('\033[1;33m-=\033[m' * 20)
    print(f'\033[34mA área do seu terreno e de \033[m{m:.1f}\033[34mm\033[m')
    print('\033[1;33m-=\033[m' * 20)
    print('\033[1;32mFIM\033[m')


print('\033[1;35mCONTROLE DE TERRENOS\033[m')
print('\033[33m--------------------\033[m')
area(float(input('\033[36m Largura (m):\033[m ')), float(input('\033[34m Comprimento (m):\033[m ')))
