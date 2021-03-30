'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome.'''
nome = str(input('\033[33mdigite o seu nome:\033[m ')).strip().upper()
print('\033[37mSeu nome tem Silva?\033[m {}{}{}'.format('\033[32m', 'SILVA' in nome, '\033[m'))
