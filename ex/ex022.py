### Crie um programa que leia o nome completo de uma pessoa e mostre:
### > O nome com todas as letras maiúsculas.
### > O nome com todas minúsculas.
### > Quantas letras ao todo (sem considerar espaços).
### > Quantas letras tem o primeiro nome.
nome = str(input('\033[35mDigite seu nome:\033[m ')).strip()
nome2 = nome.split()
print('\033[32m', nome.upper(), '\033[m')
print('\033[33m', nome.lower(), '\033[m')
print('\033[31m', len(nome) - nome.count(' '), '\033[m')
print('\033[34m', len(nome2[0]), '\033[m')
