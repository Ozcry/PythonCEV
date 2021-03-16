### Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente dese ângulo.
from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
coseno = cos(radians(an))
tangente = tan(radians(an))
print('O Ângulo de {:.2f} tem o seno de {:.2f}, coseno de {:.2f} e tangente {:.2f}'.format(an, seno, coseno, tangente))
