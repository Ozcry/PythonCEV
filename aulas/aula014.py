'''
enquanto não maça
    passo
pega
'''

'''
enquanto não maça
    se chao
        passo
    se buraco
        pula
    se moeda
        pega
pega
'''

### Em python
'''
while not maça:
    passo
pega
'''

'''
while not maça:
    if chao:
        passo
    if buraCO:
        pula
    if moeda:
        pega
pega
'''

### Brincando
'''
for c in range(1, 10):
    print(c)
print('Fim')
'''

'''
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')
'''

'''
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')
'''

'''
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
'''

'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer Continuar? [S/N]: ')).upper()
print('Fim')
'''

'''
n = 1
contadorpar = 0
contadorimpar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            contadorpar += 1
        else:
            contadorimpar += 1
print('Você digitou {} números PARES e {} números ÍMPARES!'.format(contadorpar, contadorimpar))
'''
