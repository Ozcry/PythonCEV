'''Crie um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.'''
n1 = float(input('Digite um valor em metros: '))
cores = {'limpa': '\033[m', 'azul': '\033[0;34m', 'ciano': '\033[0;36m', 'branco': '\033[0;30m'}
print('Valor em metros {}{}{}\ncentimetros {}{}{}\nmilimetros {}{}{}'.format(cores['azul'], n1, cores['limpa'], cores['ciano'], (n1 / 0.01), cores['limpa'], cores['branco'], (n1 / 0.0010000), cores['limpa']))

### Outro metodo
#n1 = int(input('Digite um valor em metros: '))
#c = n1 / 0.01
#m = n1 / 0.0010000
#print('Valor em metros {}, centimetros {}, milimetros {}.'.format(n1, c, m))
