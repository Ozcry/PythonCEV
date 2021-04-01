'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''
print('\033[1;33m-=\033[m' * 20)
print('\033[1;36mTABUADA\033[m \033[34m- digite qualquer número negativo para sair\033[m')
print('\033[1;33m-=\033[m' * 20)
while True:
    n1 = int(input('\033[35mDigite um número para ver sua tabuada:\033[m '))
    if n1 >= 0:
        for c in range(1,11):
            print(f'{n1} * {c} = {n1 * c}')
        print('\033[1;33m-=\033[m' * 20)
    elif n1 < 0:
        break
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
