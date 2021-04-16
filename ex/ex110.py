'''Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
informações geradas pelas funções que já temos no módulo criado até aqui.'''
from utilidadesCeV import moeda
print('\033[1;33m-=\033[m' * 20)
n1 = float(input('\033[34mDigite o preço: R$\033[m'))
por = int(input('\033[35mQuantos porcentos deseja aumentar ou diminuir? \033[m'))
moeda.resumo(n1, por)
