'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0,
com uma pausa de 1 sec entre eles.
'''
from time import sleep
print('\033[1;34mContagem para os fogos de artificio\033[m')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('\033[1;31mBOOOOOOM!!!\033[m')
