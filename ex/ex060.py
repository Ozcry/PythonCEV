'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
ex:. 5! = 5 x 4 x 3 x 2 x 1 = 120  (while é for)'''
print('\033[1;33m-=\033[m' * 20)
n1 = int(input('\033[36mDigite um número:\033[m '))
fatorial = 1
contador = 1
while contador <= n1:
    fatorial = fatorial * contador
    contador += 1
print('O fatorial de {}{}{} é {}{}{}'.format('\033[34m', n1, '\033[m', '\033[35m', fatorial, '\033[m'))
print('\033[1;33m-=\033[m' * 20)

### Utilizando FOR
'''
print('\033[1;33m-=\033[m' * 20)
n1 = int(input('\033[36mDigite um número:\033[m '))
fatorial = 1
for c in range(1, n1 + 1):
    fatorial = fatorial * c
print('O fatorial de {}{}{} é {}{}{}'.format('\033[34m', n1, '\033[m', '\033[35m', fatorial, '\033[m'))
print('\033[1;33m-=\033[m' * 20)
'''
