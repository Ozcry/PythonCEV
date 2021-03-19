### Escreva um programa que leia a velocidade de um carro.
### Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
### A multa vai custar R$7,00 por cada Km acima do limite.
v = float(input('Digite a velocidade do carro: '))
m = (v - 80) * 7
if v > 80:
    print('Você foi multado!')
    print('O Valor da sua multa e de R${:.2f}'.format(m))
    print('-----------')
else:
    print('Parabêns! dentro do limite permitido.')
    print('-----------')

