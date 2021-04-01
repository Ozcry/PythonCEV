'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custum mais de R$1000.
C) Qual é o nome do produto mais barato.'''
total = 0
mais1000 = 0
precomenor = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
maisbarato = ''
print('\033[1;33m-=\033[m' * 20)
while True:
    nome = str(input('\033[31mDigite o nome do produto: \033[m'))
    preco = float(input('\033[34mDigite o preço: R$\033[m'))
    total += preco
    if preco > 1000:
        mais1000 += 1
    if preco < precomenor:
        precomenor = preco
        maisbarato = nome
    continar = str(input('\033[35mContinuar [S/N]:\033[m ')).strip().upper()[0]
    if continar == 'N':
        break
    print('\033[1;33m-=\033[m' * 20)
print('\033[1;33m-=\033[m' * 20)
if mais1000 == 1:
    print(f'\033[36mO produto mais barato e {maisbarato.capitalize()}\nNo total {mais1000} produto custa mais que R$1000\nO total da compra foi R${total:.2f}\033[m')
else:
    print(f'\033[36mO produto mais barato e {maisbarato.capitalize()}\nNo total {mais1000} produtos custam mais que R$1000\nO total da compra foi R${total:.2f}\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
