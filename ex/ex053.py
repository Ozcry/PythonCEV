'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA'''
frase = str(input('\033[34mDigite sua frase:\033[m ')).strip().upper()
print('\033[1;33m-=\033[m' * 20)
dividido = frase.split()
junto = ''.join(dividido)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
if inverso == junto:
    print('\033[35mSua frase é um palíndromo\033[m')
else:
    print('\033[31mSua frase não é um palíndromo\033[m')
print('\033[1;33m-=\033[m' * 20)
### Outro jeito sem o uso do for
'''inverso2 = junto[::-1]'''
