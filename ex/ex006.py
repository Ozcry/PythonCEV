### Crie um programa que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Digite um numero: '))
cores = {'limpa': '\033[m', 'roxo': '\033[0;35m', 'azul': '\033[0;34m', 'verde': '\033[0;32m', 'vermelho': '\033[0;31m'}
print('Seu numero {}{}{}\no Dobro {}{}{}\nTriplo {}{}{}\nRaiz Quadrada {}{:.2f}{}'.format
      (cores['roxo'], n1, cores['limpa'], cores['azul'], (n1 * 2), cores['limpa'], cores['verde'], (n1 * 3), cores['limpa'], cores['vermelho'], pow(n1, (1/2)), cores['limpa']))

###Outro metodo
#n1 = int(input('Digite um numero: '))
#d = n1 * 2
#t = n1 * 3
#rq = n1 ** (1/2)
#print('Seu numero {}, o Dobro {}, Triplo {}, Raiz Quadrada {:.2f}.'.format(n1, d, t, rq))
