'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
pesome = 9999999999
pesoma = 0
print('\033[1;33m-=\033[m' * 20)
for c in range(0,5):
    peso = float(input('\033[35mDigite seu peso:\033[m '))
    if peso > pesoma:
        pesoma = peso
    if peso < pesome:
        pesome = peso
print('\033[1;33m-=\033[m' * 20)
print('\033[36mO maior peso foi\033[m {}{:.1f}{}'.format('\033[31m', pesoma, '\033[m'))
print('\033[36mO menor peso foi\033[m {}{:.1f}{}'.format('\033[32m', pesome, '\033[m'))
print('\033[1;33m-=\033[m' * 20)
