'''Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente dese ângulo.'''
from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
coseno = cos(radians(an))
tangente = tan(radians(an))
cores = {'limpa': '\033[m', 'amarelo': '\033[33m', 'branco': '\033[30m', 'vermelho': '\033[31m', 'roxo': '\033[35m'}
print('O Ângulo de {}{:.2f}{} tem o seno de {}{:.2f}{}, coseno de {}{:.2f}{} e tangente {}{:.2f}{}'.format(cores['vermelho'], an, cores['limpa'], cores['amarelo'], seno, cores['limpa'], cores['branco'], coseno, cores['limpa'], cores['roxo'], tangente, cores['limpa']))
