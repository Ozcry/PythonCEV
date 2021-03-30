'''Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.'''
n1 = float(input('Digite a altura: '))
n2 = float(input('Digite a largura: '))
print('Sua parede tem uma área de {}{:.0f}{}m², sera necessário {}{:.0f}{}L de tinta para pintá-la.'.format('\033[0;35m', (n1 * n2), '\033[m', '\033[0;32m', ((n1 * n2) / 2), '\033[m'))

###Outro metodo
#n1 = int(input('Digite a altura: '))
#n2 = int(input('Digite a largura: '))
#area = n1 * n2
#tinta = area / 2
#print('Sua parede tem uma área de {}m, sera necessário {:.0f} latas de tinta para pintá-la.'.format(area, tinta))
