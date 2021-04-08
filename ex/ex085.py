'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente.'''
print('\033[1;33m-=\033[m' * 20)
lista = [[], []]
while True:
    n1 = int(input('\033[31mDigite um valor:\033[m '))
    if n1 % 2 == 0:
        lista[0].append(n1)
    elif n1 % 2 != 0:
        lista[1].append(n1)
    sair = ' '
    while sair not in 'SN':
        continuar = str(input('\033[34mContinuar [S/N]:\033[m ')).strip().upper()[0]
        sair = continuar
    print('\033[1;33m-=\033[m' * 20)
    if sair == 'N':
        break
print(f'\033[35mOs valores pares digitados foram {sorted(lista[0])}\033[m')
print(f'\033[36mOs valores ímpares digitados foram {sorted(lista[1])}\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
