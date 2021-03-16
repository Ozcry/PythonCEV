### Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. ex: 6.127 => 6.
from math import trunc
n1 = float(input('Digite um valor: '))
print('Seu numero é {}, Sua porção inteira é {}.'.format(n1, trunc(n1)))

### Outro metodo
#n1 = float(input('Digite um valor: '))
#print('Seu numero é {}, Sua porção inteira é {}.'.format(n1, int(n1)))

