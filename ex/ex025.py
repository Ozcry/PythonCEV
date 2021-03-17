### Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome.
nome = str(input('digite o seu nome: ')).strip().upper()
print('Seu nome tem Silva? {}'.format('SILVA' in nome))
