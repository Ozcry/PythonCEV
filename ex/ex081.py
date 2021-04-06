'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados
B) A lista de valores, ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
print('\033[1;33m-=\033[m' * 20)
while True:
    lista.append(int(input('\033[36mDigite um valor:\033[m ')))
    sair = ' '
    while sair not in 'SN':
        continuar = str(input('\033[37mContinuar [S/N]: \033[m')).upper().strip()[0]
        sair = continuar
    print('\033[1;33m-=\033[m' * 20)
    if sair == 'N':
        break
lista.sort(reverse=True)
print(f'\033[35mVocê digitou {len(lista)} elementos\033[m')
print(f'\033[34mOs valores em ordem decrescente são {lista}\033[m')
if 5 in lista:
    print(f'\033[31mSim, o valor 5 esta na lista\033[m')
else:
    print('\033[31mO valor 5 não faz parte da lista\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
