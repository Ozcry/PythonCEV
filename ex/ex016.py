### Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. ex: 6.127 => 6.
from math import trunc
n1 = float(input('\033[33mDigite um valor:\033[m '))
print('\033[34mSeu numero é {}{}{}\033[m\033[34m, Sua porção inteira é \033[m{}{}{}\033[34m.\033[m'.format('\033[35m', n1,'\033[m', '\033[36m', trunc(n1), '\033[m'))

### Outro metodo
#n1 = float(input('Digite um valor: '))
#print('Seu numero é {}, Sua porção inteira é {}.'.format(n1, int(n1)))
