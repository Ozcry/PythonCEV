'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.
'''
soma = 0
for c in range(0,6):
    n = int(input('\033[34mDigite um número:\033[m '))
    if n % 2 == 0:
        soma = soma + n
print('\033[33mA Soma de todos os números PARES digitados é\033[m {}{}{}'.format('\033[36m', soma, '\033[m'))
