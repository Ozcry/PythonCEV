'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
pc = randint(1, 10)
palpites = 0
jogador = 0
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32m---- O computador escolheu um número de 1 a 10 tente adivinhar ----\033[m')
print('\033[1;33m-=\033[m' * 20)
while jogador != pc:
    n1 = int(input('Digite um número de 1 a 10: '))
    palpites += 1
    jogador = n1
    if jogador == pc:
        print('\033[34mVocê acertou,\033[m \033[1;36mPARABÊNS!!\033[m')
        print('\033[37mForam necessarias\033[m {}{}{} \033[37mtentativas para acertar\033[m'.format('\033[35m', palpites, '\033[m'))
        print('\033[1;33m-=\033[m' * 20)
    else:
        print('\033[31mVocê errou, tente novamente!\033[m')
        print('\033[1;33m-=\033[m' * 20)
