### Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar, obs(US$1,00 = R$3,27).
n1 = float(input('Quanto vc tem de dinheiro na carteira? '))
print('Você tem {} reais e pode comprar {:.2f} dolares.'.format(n1, (n1 / 3.27)))

###Outro metodo
#n1 = int(input('Quanto vc tem de dinheiro na carteira? '))
#d = n1 / 3.27
#print('Você tem {} reais e pode comprar {:.2f} dolares.'.format(n1, d))
