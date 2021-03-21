### Desenvolva um programa que pergunte a distância de uma viagem em Km.
### Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
d = float(input('\033[36mDigite a distancia:\033[m '))
p1 = d * 0.50
p2 = d * 0.45
if d < 200:
    print('\033[34mO valor da sua passagem e de R$\033[m\033[32m{:.2f}\033[m'.format(p1))
    print('\033[33m-----------\033[m')
else:
    print('\033[34mO valor da sua passagem e de R$\033[m\033[32m{:.2f}\033[m'.format(p2))
    print('\033[33m-----------\033[m')
