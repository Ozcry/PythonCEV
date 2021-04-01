'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS:. Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print('\033[1;33m-=\033[m' * 20)
print('\033[1;31mBANCO DO CEV\033[m')
print('\033[1;33m-=\033[m' * 20)
valor = int(input('Qual valor deseja sacar? '))
total = valor
cedula = 50
tcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        tcedula += 1
    else:
        if tcedula > 0:
            print(f'Total de {tcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        tcedula = 0
        if total == 0:
            break
print('\033[1;33m-=\033[m' * 20)
print('\033[32mFIM\033[m')
