'''Crie um programa que leia dois números e mostre a soma entre eles.'''
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro: '))
s = n1 + n2
cores = {'limpa': '\033[m', 'amarelo': '\033[0;33m', 'azul': '\033[0;34m', 'ciano': '\033[0;36m'}
print('A soma entre {}{}{} e {}{}{} vale {}{}{}'.format(cores['amarelo'], n1, cores['limpa'], cores['azul'], n2, cores['limpa'], cores['ciano'], s, cores['limpa']))
