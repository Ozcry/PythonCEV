### Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
### O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
n = randint(0, 5)
e = int(input('\033[33mO computador escolheu um número de 0 a 5 descubra qual é:\033[m '))
print('\033[32mPROCESSANDO...\033[m')
sleep(2)
if e == n:
    print('\033[36mParabêns vc acertou!\033[m')
else:
    print('\033[35mErrado! eu escolhi\033[m \033[31m{}\033[m \033[35mnão\033[m \033[34m{}\033[m'.format(n, e))
