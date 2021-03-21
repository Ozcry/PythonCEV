### Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
nome = input('Digite seu nome: ')
print('É um prazer te conhecer, \033[4;33m{}\033[m!'.format(nome))
