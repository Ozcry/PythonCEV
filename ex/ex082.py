'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas.'''
lista = []
listapar = []
listaimpar = []
contpar = contimpar = 0
print('\033[1;33m-=\033[m' * 20)
while True:
    n1 = int(input('\033[34mDigite um valor: \033[m'))
    if n1 in lista:
        print('\033[31mValor duplicado, Não vou adicionar...\033[m')
    else:
        lista.append(n1)
    sair = ' '
    while sair not in 'SN':
        continuar = str(input('\033[37mContinuar [S/N]:\033[m ')).strip().upper()[0]
        sair = continuar
    if sair == 'N':
        break
    print('\033[1;33m-=\033[m' * 20)
for v in lista:
    if v % 2 == 0:
        listapar.append(v)
        contpar += 1
    elif v % 2 != 0:
        listaimpar.append(v)
        contimpar += 1
print('\033[1;33m-=\033[m' * 20)
print(f'\033[36mA lista completa é {lista}\033[m')
if contpar != 0:
    print(f'\033[35mA lista de pares é {listapar}\033[m')
else:
    print('\033[31mNão ouve números PARES\033[m')
if contimpar != 0:
    print(f'\033[34mA lista ímpar é {listaimpar}\033[m')
else:
    print('\033[31mNão ouve números ÍMPARES\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
