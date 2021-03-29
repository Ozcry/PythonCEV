'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
maior = 0
menor = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
contador = 0
soma = 0
sair = 0
respostac = ''
print('\033[1;33m-=\033[m' * 20)
while sair == 0:
    n1 = int(input('\033[32mDigite um número:\033[m '))
    soma += n1
    contador += 1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    continuar = str(input('Deseja continuar [\033[34mS\033[m/\033[35mN\033[m]: ')).strip().upper()[0]
    print('\033[1;33m-=\033[m' * 20)
    if continuar == 'N':
        sair += 1
    elif continuar == 'S':
        sair = 0
    else:
        print('\033[1;31mOPÇÃO INVALIDA\033[m')
        print('\033[1;33m-=\033[m' * 20)
print('O maior valor digitado foi {}{}{}'.format('\033[36m', maior, '\033[m'))
print('O menor valor digitado foi {}{}{}'.format('\033[33m', menor, '\033[m'))
print('A média entre os números digitados foi {}{:.1f}{}'.format('\033[32m', soma / contador, '\033[m'))
print('\033[1;33m-=\033[m' * 20)
