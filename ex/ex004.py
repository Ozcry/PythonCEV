'''Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiceis sobre ele.'''
n = str(input('Digite algo: '))
print('\033[4;37m', type(n), '\033[m')
print('\033[0;31m', n.isupper(), '\033[m')
print('\033[0;32m', n.istitle(), '\033[m')
print('\033[0;33m', n.isspace(), '\033[m')
print('\033[0;34m', n.isprintable(), '\033[m')
print(' Apenas um teste {}{}{}'.format('\033[0;35m', n.isnumeric(), '\033[m'))
print('\033[0;36m', n.islower(), '\033[m')
print('\033[0;37m', n.isidentifier(), '\033[m')
print('\033[0;30m', n.isdigit(), '\033[m')
print('\033[40m', n.isdecimal(), '\033[m')
print('\033[41m', n.isascii(), '\033[m')
print('\033[42m', n.isalpha(), '\033[m')
