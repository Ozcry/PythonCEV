'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''
v = float(input('\033[34mDigite a velocidade do carro:\033[m '))
m = (v - 80) * 7
if v > 80:
    print('\033[31mVocê foi multado!\033[m')
    print('\033[30mO Valor da sua multa e de R$\033[m\033[32m{:.2f}\033[m'.format(m))
    print('\033[33m-----------\033[m')
else:
    print('\033[36mParabêns! dentro do limite permitido.\033[m')
    print('\033[33m-----------\033[m')
