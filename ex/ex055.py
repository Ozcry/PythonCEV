'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
pesome = 99999999999999999999999999999
pesoma = 0
print('\033[1;33m-=\033[m' * 20)
for c in range(0, 5):
    peso = float(input('\033[35mDigite o peso da {}ª pessoa:\033[m '.format(c + 1)))
    if peso > pesoma:
        pesoma = peso
    if peso < pesome:
        pesome = peso
print('\033[1;33m-=\033[m' * 20)
print('\033[36mO maior peso foi\033[m {}{:.1f}{}'.format('\033[31m', pesoma, '\033[m'))
print('\033[36mO menor peso foi\033[m {}{:.1f}{}'.format('\033[32m', pesome, '\033[m'))
print('\033[1;33m-=\033[m' * 20)
