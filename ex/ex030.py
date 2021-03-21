### Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
from time import sleep
n = int(input('\033[31mDigite um número:\033[m '))
print('\033[32mPROCESSANDO...\033[m')
sleep(2)
if n % 2 == 0:
    print('\033[35mSeu numero e PAR!\033[m')
    print('\033[33m-----------\033[m')
else:
    print('\033[35mSeu número e IMPAR!\033[m')
    print('\033[33m-----------\033[m')
