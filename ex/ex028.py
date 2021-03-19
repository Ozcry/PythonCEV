### Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
### O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
n = randint(0, 5)
e = int(input('O computador escolheu um número de 0 a 5 descubra qual é: '))
print('PROCESSANDO...')
sleep(2)
if e == n:
    print('Parabêns vc acertou!')
else:
    print('Errado! eu escolhi {} não {}'.format(n, e))
