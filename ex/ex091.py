'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
print('\033[1;33m-=\033[m' * 20)
jogos = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
for i, c in jogos.items():
    print(f'\033[34m{i} tirou {c} no dado\033[m')
    sleep(0.5)
print('\033[1;33m-=\033[m' * 20)
sleep(0.5)
jogosordendo = sorted(jogos.items(), key=lambda x: x[1], reverse=True)
print(f'\033[1;36m{"== RANKING DOS JOGADORES ==":^30}\033[m')
for i, c in enumerate(jogosordendo):
    print(f'\033[35m  {i + 1}º lugar: {c[0]} com {c[1]}\033[m')
    sleep(0.5)
print('\033[1;33m-=\033[m' * 20)
sleep(0.5)
print('\033[1;32mFIM\033[m')
