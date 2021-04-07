'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
lista = list()
jogos = list()
print('\033[1;33m-=\033[m' * 20)
print('           JOGA NA MEGA SENA     ')
print('\033[1;33m-=\033[m' * 20)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print('\033[1;33m-=\033[m' * 20)
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('\033[1;33m-=\033[m' * 20)
print('FIM')

###Outro metodo
'''
from time import sleep
import random
print('\033[1;33m-=\033[m' * 20)
print('            JOGA NA MEGA SENA           ')
print('\033[1;33m-=\033[m' * 20)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(1, jogos + 1):
    print(f'Jogo {c}: {sorted(random.sample(range(1, 60), k = 6))}')
    sleep(1)
print('\033[1;33m-=\033[m' * 20)
print('FIM')
'''
