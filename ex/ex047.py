'''
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''
print('\033[1;33m-=\033[m' * 20)
print('\033[1;36mNúmeros PARES de 1 a 50\033[m')
from time import sleep
for c in range(2, 51, 2):
        print(c)
        sleep(0.25)
print('\033[1;32mFIM\033[m')
print('\033[1;33m-=\033[m' * 20)

### Outro metodo
'''
print('\033[1;33m-=\033[m' * 20)
print('\033[1;36mNúmeros PARES de 1 a 50\033[m')
from time import sleep
for c in range(1, 51):
    if c % 2 == 0:
        print(c)
        sleep(0.25)
print('\033[1;32mFIM\033[m')
print('\033[1;33m-=\033[m' * 20)
'''
