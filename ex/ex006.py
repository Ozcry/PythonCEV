### Crie um programa que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Digite um numero: '))
print('Seu numero {}\no Dobro {}\nTriplo {}\nRaiz Quadrada {:.2f}'.format(n1, (n1 * 2), (n1 * 3), pow(n1, (1/2))))

###Outro metodo
#n1 = int(input('Digite um numero: '))
d = n1 * 2
t = n1 * 3
rq = n1 ** (1/2)
#print('Seu numero {}, o Dobro {}, Triplo {}, Raiz Quadrada {:.2f}.'.format(n1, d, t, rq))