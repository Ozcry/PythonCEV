'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas.'''
lista = []
listapar = []
listaimpar = []
contpar = contimpar = 0
print('\033[1;33m-=\033[m' * 20)
while True:
    n1 = int(input('Digite um valor: '))
    if n1 in lista:
        print('Valor duplicado, Não vou adicionar...')
    else:
        lista.append(n1)
    sair = ' '
    while sair not in 'SN':
        continuar = str(input('Continuar [S/N]: ')).strip().upper()[0]
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
print(f'A lista completa é {lista}')
if contpar != 0:
    print(f'A lista de pares é {listapar}')
else:
    print('Não ouve números PARES')
if contimpar != 0:
    print(f'A lista ímpar é {listaimpar}')
else:
    print('Não ouve números ÍMPARES')
print('\033[1;33m-=\033[m' * 20)
print('FIM')
