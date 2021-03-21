### O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostra a ordem sorteada.
from random import shuffle
n1 = str(input('\033[37mDigite o primeiro nome:\033[m '))
n2 = str(input('\033[36mDigite o segundo nome:\033[m '))
n3 = str(input('\033[35mDigite o terceiro nome:\033[m '))
n4 = str(input('\033[34mDigite o quarto nome:\033[m '))
nomes = [n1, n2, n3, n4]
shuffle(nomes)
print('\033[33mOrdem de apresentação =>\033[m {}{}{}'.format('\033[32m', nomes, '\033[m'))
