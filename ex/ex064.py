'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''
n1 = 0
contador = 0
soma = 0
print('\033[1;33m-=\033[m' * 20)
print('\033[1;36mPara sair do programa digite ''999''\033[m ')
print('\033[1;33m-=\033[m' * 20)
while n1 != 999:
    n1 = int(input('\033[32mdigite um número:\033[m '))
    if n1 != 999:
        contador += 1
        soma += n1
print('\033[1;33m-=\033[m' * 20)
print('Você digitou {}{}{} números e a soma entre eles é {}{}{}'.format('\033[34m', contador, '\033[m', '\033[35m', soma, '\033[m'))
print('\033[1;33m-=\033[m' * 20)
