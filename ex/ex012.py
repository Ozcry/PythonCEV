### Crie um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
n1 = float(input('Preço do produto: '))
print('Preço do produto {}{}{}, com o desconto {}{:.2f}{}'.format('\033[0;33m', n1, '\033[m', '\033[0;37m', (n1 - (n1 * 5 / 100)), '\033[m'))

###Outro metodo
#n1 = int(input('Preço do produto: '))
#d = n1 * 0.05
#f = n1 - d
#print('Preço do produto {}, com o desconto {}'.format(n1, f))
