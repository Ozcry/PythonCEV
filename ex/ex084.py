'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves'''
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

### Outro metodo
'''
print('\033[1;33m-=\033[m' * 20)
lista = []
lista2 = []
pesado = []
leve = []
maior = menor = cont = 0
while True:
    nome = str(input('Digite seu nome: '))
    peso = float(input('Digite seu peso: '))
    cont += 1
    lista.append(nome)
    lista.append(peso)
    lista2.append(lista[:])
    lista.clear()
    if cont == 1:
        maior = peso
        menor = peso
        pesado.append(nome)
        leve.append(nome)
    if peso < menor:
        menor = peso
        leve.clear()
        leve.append(nome)
    elif peso == menor:
        leve.append(nome)
    elif peso > maior:
        maior = peso
        pesado.clear()
        pesado.append(nome)
    elif peso == maior:
        pesado.append(nome)
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Continuar [S/N]: ')).strip().upper()[0]
    if sair == 'N':
        break
    print('\033[1;33m-=\033[m' * 20)
print('\033[1;33m-=\033[m' * 20)
print(f'Ao todo, você cadastrou {cont} pessoas')
print(f'O maior peso foi de {maior}, peso de {pesado}')
print(f'O menor peso foi de {menor}, peso de {leve}')
print('\033[1;33m-=\033[m' * 20)
print('FIM')
'''
