'''Crie um programa onde o usuário posso digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
print('\033[1;33m-=\033[m' * 20)
lista = []
for c in range(0, 5):
    n1 = int(input('\033[34mDigite um valor:\033[m '))
    if c == 0 or n1 > lista[-1]:
        lista.append(n1)
        print('\033[31mAdicionado ao final da lista...\033[m')
        print('\033[1;33m-=\033[m' * 20)
    else:
        pos = 0
        while pos < len(lista):
            if n1 <= lista[pos]:
                lista.insert(pos, n1)
                print(f'\033[35mAdicionando na posição {pos} da lista...\033[m')
                print('\033[1;33m-=\033[m' * 20)
                break
            pos += 1
print(f'\033[36mOs valores digitados em ordem foram {lista}\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')

### Outro metodo
'''
lista = []
print('\033[1;33m-=\033[m' * 20)
while True:
    if len(lista) == 0:
        n1 = int(input('Digite um valor: '))
        lista.append(n1)
        print('Adicionado ao final da lista...')
        print('\033[1;33m-=\033[m' * 20)
    if len(lista) == 1:
        n1 = int(input('Digite um valor: '))
        if n1 < lista[0]:
            lista.insert(0, n1)
            print(f'Adicionado na posição {lista.index(n1) + 1} da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif n1 > lista[0]:
            lista.append(n1)
            print('Adicionado ao final da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif n1 in lista:
            print('Valor duplicado! Não vou adicionar...')
            print('\033[1;33m-=\033[m' * 20)
    if len(lista) == 2:
        n1 = int(input('Digite um valor: '))
        if n1 > lista[1]:
            lista.append(n1)
            print('Adicionado ao final da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif n1 < lista[0]:
            lista.insert(0, n1)
            print(f'Adicionado na posição {lista.index(n1) + 1} da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif lista[0] < n1 < lista[1]:
            lista.insert(1, n1)
            print(f'Adicionado na posição {lista.index(n1) + 1} da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif n1 in lista:
            print('Valor duplicado! Não vou adicionar...')
            print('\033[1;33m-=\033[m' * 20)
    if len(lista) == 3:
        n1 = int(input('Digite um valor: '))
        if n1 < lista[0]:
            lista.insert(0, n1)
            print(f'Adicionado na posição {lista.index(n1) + 1} da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif n1 > lista[2]:
            lista.append(n1)
            print('Adicionado ao final da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif lista[1] < n1 < lista[2]:
            lista.insert(2, n1)
            print(f'Adicionado na posição {lista.index(n1) + 1} da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif lista[0] < n1 < lista[1]:
            lista.insert(1, n1)
            print(f'Adicionado na posição {lista.index(n1) + 1} da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif n1 in lista:
            print('Valor duplicado! Não vou adicionar...')
            print('\033[1;33m-=\033[m' * 20)
    if len(lista) == 4:
        n1 = int(input('Digite um valor: '))
        if n1 < lista[0]:
            lista.insert(0, n1)
            print(f'Adicionado na posição {lista.index(n1) + 1} da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif n1 > lista[3]:
            lista.append(n1)
            print('Adicionado ao final da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif lista[0] < n1 < lista[1]:
            lista.insert(1, n1)
            print(f'Adicionado na posição {lista.index(n1) + 1} da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif lista[1] < n1 < lista[2]:
            lista.insert(2, n1)
            print(f'Adicionado na posição {lista.index(n1) + 1} da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif lista[2] < n1 < lista[3]:
            lista.insert(3, n1)
            print(f'Adicionado na posição {lista.index(n1) + 1} da lista...')
            print('\033[1;33m-=\033[m' * 20)
        elif n1 in lista:
            print('Valor duplicado! Não vou adicionar...')
            print('\033[1;33m-=\033[m' * 20)
    if len(lista) == 5:
        break
print(f'Os números digitados foram {lista}')
print('\033[1;33m-=\033[m' * 20)
print('FIM')
'''