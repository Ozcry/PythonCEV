'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça
também um programa que inporte esse módulo e use algumas dessas funções.'''
from utilidadesCeV import moeda
print('\033[1;33m-=\033[m' * 20)
n1 = float(input('\033[34mDigite o preço: R$\033[m'))
por = int(input('\033[35mQuantos porcentos deseja aumentar ou diminuir?\033[m '))
print(f'\033[33mA metade de R${n1:.2f} é R${moeda.metade(n1):.2f}\033[m')
print(f'\033[31mO dobro de R${n1:.2f} é R${moeda.dobro(n1):.2f}\033[m')
if por > 0:
    print(f'\033[36mAumentando {por}%, temos R${moeda.aumento(n1, por):.2f}\033[m')
elif por < 0:
    print(f'\033[36mDiminuindo {por * -1}%, temos R${moeda.aumento(n1, por):.2f}\033[m')
else:
    print(f'\033[36mO preço continua o mesmo {n1:.2f}\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
