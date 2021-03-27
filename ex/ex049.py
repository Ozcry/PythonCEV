'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
print('\033[1;33m-=\033[m' * 20)
print('\033[32m---------\033[m\033[1;34mTABUADA\033[m\033[32m---------\033[m')
n1 = int(input('\033[36mDigite um número:\033[m '))
for c in range(1, 11):
    print('{} * {} = {}'.format(n1, c, n1 * c))
print('\033[32m---------\033[m\033[1;34mFIM\033[m\033[32m---------\033[m')
print('\033[1;33m-=\033[m' * 20)

### Outro metodo
'''
print('\033[1;33m-=\033[m' * 20)
print('\033[32m---------\033[m\033[1;34mTABUADA\033[m\033[32m---------\033[m')
n1 = int(input('\033[36mDigite um número:\033[m '))
for c in range(1,11):
    mult = n1 * c
    print('{} * {} = {}'.format(n1, c, mult))
print('\033[32m---------\033[m\033[1;34mFIM\033[m\033[32m---------\033[m')
print('\033[1;33m-=\033[m' * 20)
'''
