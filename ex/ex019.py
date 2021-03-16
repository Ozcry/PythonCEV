### Um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele. lendo o nome deles e escrevendo o nome escolhido.
from random import choice
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
r = choice([n1, n2, n3, n4])
print('O escolhido foi {}'.format(r))
