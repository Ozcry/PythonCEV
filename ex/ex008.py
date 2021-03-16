### Crie um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
n1 = float(input('Digite um valor em metros: '))
print('Valor em metros {}\ncentimetros {}\nmilimetros {}.'.format(n1, (n1 / 0.01), (n1 / 0.0010000)))

### Outro metodo
#n1 = int(input('Digite um valor em metros: '))
#c = n1 / 0.01
#m = n1 / 0.0010000
#print('Valor em metros {}, centimetros {}, milimetros {}.'.format(n1, c, m))