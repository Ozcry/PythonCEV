'''Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''
from time import sleep
n1 = int(input('\033[33mDigite o primeiro número:\033[m '))
n2 = int(input('\033[33mDigite o segundo número:\033[m '))
cores = {'limpa': '\033[m', 'ciano': '\033[36m', 'azul': '\033[34m'}
print('\033[32mPROCESSANDO...\033[m')
sleep(2)
if n1 > n2:
    print('O primeiro valor de {}{}{} é maior do que {}{}{}'.format(cores['ciano'], n1, cores['limpa'], cores['azul'], n2, cores['limpa']))
elif n2 > n1:
    print('O segundo valor de {}{}{} é maior do que {}{}{}'.format(cores['azul'], n2, cores['limpa'], cores['ciano'], n1, cores['limpa']))
else:
    print('Não existe valor maior, {}{}{} é {}{}{} são iguais'.format(cores['ciano'], n1, cores['limpa'], cores['azul'], n2, cores['limpa']))
