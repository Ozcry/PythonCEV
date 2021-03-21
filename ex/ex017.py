### Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
hipo = hypot(n1, n2)
cores = {'limpa': '\033[m', 'azul': '\033[34m', 'verde': '\033[32m', 'ciano': '\033[36m'}
print('Cateto Oposto {}{:.2f}{}\nCateto Adjacente {}{:.2f}{}\nHipotenusa {}{:.2f}{}'.format(cores['ciano'], n1, cores['limpa'], cores['verde'], n2, cores['limpa'], cores['azul'], hipo, cores['limpa']))

### Outro metodo
#from math import sqrt
#n1 = float(input('Comprimento do cateto oposto: '))
#n2 = float(input('Comprimento do cateto adjacente: '))
#hipo = sqrt(n1 ** 2 + n2 ** 2)
#print('Cateto Oposto {:.2f}\nCateto Adjacente {:.2f}\nHipotenusa {:.2f}'.format(n1, n2, hipo))
