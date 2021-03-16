### O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostra a ordem sorteada.
from random import shuffle
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
nomes = [n1, n2, n3, n4]
shuffle(nomes)
print('Ordem de apresentação => {}'.format(nomes))
