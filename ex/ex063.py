'''Escreva um programa que leia um número 'n' inteiro qualquer e mostre na tela os 'n'
primeiros elementos de uma Sequência de Fibonacci.
Ex:. 0 - 1 - 1 - 2 - 3 - 5 - 8'''
print('\033[1;33m-=\033[m' * 20)
n1 = int(input('\033[34mDigite um número:\033[m '))
t1 = 0
t2 = 1
cont = 3
print('{} - {}'.format(t1, t2), end='')
while cont <= n1:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -\033[35m FIM\033[m')
print('\033[1;33m-=\033[m' * 20)