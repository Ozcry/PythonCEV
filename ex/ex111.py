'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todos as
funções utilizadas nos DESAFIOS 107, 108 e 109 para o primerio pacote e mantenha tudo funcionado.'''
from utilidadesCeV import moeda
print('\033[1;33m-=\033[m' * 20)
n1 = float(input('\033[34mDigite o preço: R$\033[m'))
por = int(input('\033[35mQuantos porcentos deseja aumentar ou diminuir? \033[m'))
moeda.resumo(n1, por)
