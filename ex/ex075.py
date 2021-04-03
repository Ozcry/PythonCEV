'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares.'''
print('\033[1;33m-=\033[m' * 20)
quatro = (int(input('\033[34mDigite um número: \033[m')), int(input('\033[35mDigite outro número: \033[m')), int(input('\033[36mDigite mais um número:\033[m ')), int(input('\033[37mDigite o último número:\033[m ')))
print('\033[1;33m-=\033[m' * 20)
print(f'\033[31mO valor 9 apareceu {quatro.count(9)} vezes\033[m')
if 3 in quatro:
    print(f'\033[33mO valor 3 apareceu na {quatro.index(3) + 1}ª posição\033[m')
else:
    print('\033[34mO valor 3 não foi digitado\033[m')
print(f'\033[35mOs valores pares digitados foram\033[m ', end='')
for c in quatro:
    if c % 2 == 0:
        print(f'\033[35m{c}\033[m ', end='')
print('\n')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')

### Outro Metodo
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
quatro = (n1, n2, n3, n4)
cont = 0
posicao2 = 0
posicao3 = 0
print(f'Os valores pares digitados foram ', end='')
for c in quatro:
    if c == 9:
        cont += 1
    if c == 3:
        posicao = quatro.index(3) + 1
        posicao2 = posicao
        posicao3 += 1
    if c % 2 == 0:
        if c != quatro[-1]:
            print(f'{c}, ', end='')
        else:
            print(c, end='')
print(f'\nO valor 9 apareceu {cont} vezes')
if posicao2 != 0:
    print(f'O valor 3 apareceu na {posicao2}ª posição')
if posicao3 == 0:
    print('O valor 3 não foi digitado')

'''
