'''Faça um programa que leia um número inteiro e diga se ele e ou não um número primo.'''
num = int(input('\033[32mDigite um número:\033[m '))
print('\033[1;33m-=\033[m' * 20)
tot = 0
if num <= 1:
    print('\033[31mSeu número não é PRIMO\033[m')
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
if tot == 2:
    print('\033[34mSeu número é PRIMO\033[m')
elif tot > 2:
    print('\033[31mSeu número não é PRIMO\033[m')
