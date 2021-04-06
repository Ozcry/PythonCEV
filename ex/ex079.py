'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = []
print('\033[1;33m-=\033[m' * 20)
while True:
    n1 = int(input('\033[34mDigite um valor:\033[m '))
    if n1 not in lista:
        lista.append(n1)
        print('\033[32mValor adicionado com sucesso...\033[m')
    elif n1 in lista:
        print('\033[31mValor duplicado! Não vou adicionar...\033[m')
    sair = ' '
    while sair not in 'SN':
        continuar = str(input('\033[37mContinuar [S/N]:\033[m ')).strip().upper()[0]
        sair = continuar
    if sair in 'N':
        break
    print('\033[1;33m-=\033[m' * 20)
print('\033[1;33m-=\033[m' * 20)
print(f'\033[35mVocê digitou os valores {sorted(lista)}\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
