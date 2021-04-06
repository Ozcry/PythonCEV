'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista'''
print('\033[1;33m-=\033[m' * 20)
lista = []
mai = []
men = []
for c in range(0, 5):
    lista.append(int(input('\033[34mDigite um valor:\033[m ')))
for i, c in enumerate(lista):
    if c == max(lista):
        mai.append(i + 1)
    if c == min(lista):
        men.append(i + 1)
print('\033[1;33m-=\033[m' * 20)
print(f'\033[35mVocê digitou os valores {lista}\033[m')
print(f'\033[36mO maior valor digitado foi {max(lista)}, nas posições {mai}\033[m')
print(f'\033[31mO menor valor digitado foi {min(lista)}, nas posições {men}\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
