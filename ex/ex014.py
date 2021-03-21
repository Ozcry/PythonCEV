### Crie um programa que converta uma temperatura digitada em c e converta para f
n1 = float(input('Digite a temperatura em °C: '))
print('sua temperatura em Celsius {}{}°C{}\nem Fahrenheit {}{}°F{}'.format('\033[0;33m', n1, '\033[m', '\033[34m', ((n1 * 1.8) + 32), '\033[m'))
