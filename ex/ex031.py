### Desenvolva um programa que pergunte a distância de uma viagem em Km.
### Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
d = float(input('Digite a distancia: '))
p1 = d * 0.50
p2 = d * 0.45
if d < 200:
    print('O valor da sua passagem e de R${:.2f}'.format(p1))
    print('-----------')
else:
    print('O valor da sua passagem e de R${:.2f}'.format(p2))
    print('-----------')
