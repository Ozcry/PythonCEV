'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele. lendo o nome deles e escrevendo o nome escolhido.'''
from random import choice
n1 = str(input('\033[31mDigite o primeiro nome:\033[m '))
n2 = str(input('\033[32mDigite o segundo nome:\033[m '))
n3 = str(input('\033[33mDigite o terceiro nome:\033[m '))
n4 = str(input('\033[34mDigite o quarto nome:\033[m '))
r = choice([n1, n2, n3, n4])
print('\033[35mO escolhido foi\033[m {}{}{}'.format('\033[36m', r, '\033[m'))
