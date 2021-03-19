### Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
from time import sleep
n = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(2)
if n % 2 == 0:
    print('Seu numero e PAR!')
    print('-----------')
else:
    print('Seu número e IMPAR!')
    print('-----------')
