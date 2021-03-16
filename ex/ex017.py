### Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
hipo = hypot(n1, n2)
print('Cateto Oposto {:.2f}\nCateto Adjacente {:.2f}\nHipotenusa {:.2f}'.format(n1, n2, hipo))

### Outro metodo
#from math import sqrt
#n1 = float(input('Comprimento do cateto oposto: '))
#n2 = float(input('Comprimento do cateto adjacente: '))
#hipo = sqrt(n1 ** 2 + n2 ** 2)
#print('Cateto Oposto {:.2f}\nCateto Adjacente {:.2f}\nHipotenusa {:.2f}'.format(n1, n2, hipo))