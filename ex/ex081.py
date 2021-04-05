'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados
B) A lista de valores, ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
lista.sort(reverse=True)
cont = 0
print('\033[1;33m-=\033[m' * 20)
while True:
    n1 = int(input('Digite um valor: '))
    lista.append(n1)
    cont += 1
    sair = ' '
    while sair not in 'SN':
        continuar = str(input('Continuar [S/N]: ')).upper().strip()[0]
        sair = continuar
    print('\033[1;33m-=\033[m' * 20)
    if sair == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {cont} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'Sim, o valor 5 esta na lista')
elif 5 not in lista:
    print('O valor 5 não faz parte da lista')
print('\033[1;33m-=\033[m' * 20)
print('FIM')
