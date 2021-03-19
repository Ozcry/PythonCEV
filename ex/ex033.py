### Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print('Maior número {:.1f}'.format(n1))
if n2 > n1 and n2 > n3:
    print('Maior número {:.1f}'.format(n2))
if n3 > n1 and n3 > n2:
    print('Maior número {:.1f}'.format(n3))
if n1 < n2 and n1 < n3:
    print('Menor número {:.1f}'.format(n1))
if n2 < n1 and n2 < n3:
    print('Menor número {:.1f}'.format(n2))
if n3 < n1 and n3 < n2:
    print('Menor número {:.1f}'.format(n3))
print('----------')
