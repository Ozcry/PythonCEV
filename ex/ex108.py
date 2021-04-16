'''Adapte o código do DESAFIO 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um
valor monetário formatodo.'''
from utilidadesCeV import moeda
print('\033[1;33m-=\033[m' * 20)
n1 = float(input('\033[34mDigite o preço: R$\033[m'))
por = int(input('\033[33mQuantos porcentos deseja aumentar ou diminuir?\033[m '))
print(f'\033[35mA metade de {moeda.moeda(n1)} é {moeda.moeda(moeda.metade(n1))}\033[m')
print(f'\033[36mO dobro de {moeda.moeda(n1)} é {moeda.moeda(moeda.dobro(n1))}\033[m')
if por > 0:
    print(f'\033[31mAumentando {por}%, temos {moeda.moeda(moeda.aumento(n1, por))}\033[m')
elif por < 0:
    print(f'\033[31mDiminuindo {por * -1}%, temos {moeda.moeda(moeda.aumento(n1, por))}\033[m')
else:
    print(f'\033[31mO preço continua o mesmo {moeda.moeda(n1)}\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
