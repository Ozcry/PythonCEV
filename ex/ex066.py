'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)'''
print('\033[1;33m-=\033[m' * 20)
cont = 0
soma = 0
while True:
    n1 = int(input('\033[31mDigite um número (999 para parar):\033[m '))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print('\033[1;33m-=\033[m' * 20)
print(f'\033[34mForam Digitados {cont} númeors e a soma entre eles é {soma}\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
