'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista'''
print('\033[1;33m-=\033[m' * 20)
lista = []
mai = []
men = []
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
for i, c in enumerate(lista):
    if c == max(lista):
        mai.append(i + 1)
    if c == min(lista):
        men.append(i + 1)
print('\033[1;33m-=\033[m' * 20)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)}, nas posições {indicesm}')
print(f'O menor valor digitado foi {min(lista)}, nas posições {indicesn}')
print('\033[1;33m-=\033[m' * 20)
print('FIM')
