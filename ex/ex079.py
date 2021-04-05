'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = []
print('\033[1;33m-=\033[m' * 20)
while True:
    n1 = int(input('Digite um valor: '))
    if n1 not in lista:
        lista.append(n1)
        print('Valor adicionado com sucesso...')
    elif n1 in lista:
        print('Valor duplicado! Não vou adicionar...')
    sair = ' '
    while sair not in 'SN':
        continuar = str(input('Continuar [S/N]: ')).strip().upper()[0]
        sair = continuar
    if sair in 'N':
        break
    print('\033[1;33m-=\033[m' * 20)
print('\033[1;33m-=\033[m' * 20)
print(f'Você digitou os valores {sorted(lista)}')
print('\033[1;33m-=\033[m' * 20)
print('FIM')
