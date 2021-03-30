'''Crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
> unidade: 4
> dezena: 3
> centena: 8
> milhar: 1'''
n1 = int(input('\033[36mDigite um número entre 0  e 9999:\033[m '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('unidade: {}{}{}'.format('\033[35m', u, '\033[m'))
print('dezena: {}{}{}'.format('\033[34m', d, '\033[m'))
print('centena: {}{}{}'.format('\033[33m', c, '\033[m'))
print('milhar: {}{}{}'.format('\033[32m', m, '\033[m'))
