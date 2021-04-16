'''Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um parâmetro a mais, informando se o
valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvidada no DESAFIO 108.'''
from utilidadesCeV import moeda
print('\033[1;33m-=\033[m' * 20)
n1 = float(input('\033[34mDigite o preço: R$\033[m'))
por = int(input('\033[35mQuantos porcentos deseja aumentar ou diminuir?\033[m '))
print(f'\033[36mA metade de {moeda.moeda(n1)} é {moeda.metade(n1, True)}\033[m')
print(f'\033[33mO dobro de {moeda.moeda(n1)} é {moeda.metade(n1, True)}\033[m')
if por > 0:
    print(f'\033[31mAumentando {por}%, temos {moeda.aumento(n1, por, True)}\033[m')
elif por < 0:
    print(f'\033[31mDiminuindo {por * -1}%, temos {moeda.aumento(n1, por, True)}\033[m')
else:
    print(f'\033[31mO preço continua o mesmo {moeda.moeda(n1)}\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
