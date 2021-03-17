### Crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
### Ex: Digite um número: 1834
### unidade: 4
### dezena: 3
### centena: 8
### milhar: 1
n1 = int(input('Digite um número entre 0  e 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
