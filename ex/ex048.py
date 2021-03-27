'''
Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no
intervalo de 1 até 500.
'''
print('\033[1;33m-=\033[m' * 20)
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c
print('\033[35mExiste\033[m {}{}{} \033[35mnúmeros entre 1 e 500 que são impares e múltiplos de três a soma deles e\033[m {}{}{}'.format('\033[34m', contador, '\033[m', '\033[34m', soma, '\033[m'))
print('\033[1;33m-=\033[m' * 20)

### Outro metodo
'''
print('\033[1;33m-=\033[m' * 20)
soma = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c
print('\033[35mA Soma entre todos os números entre 1 e 500 que são impares e múltiplos de três é\033[m {}{}{}'.format('\033[34m', soma, '\033[m'))
print('\033[1;33m-=\033[m' * 20)
'''
