### Interrompendo while
'''
enquanto verdadeiro
    se bloco
        passo
    se buraco
        pula
    se moeda
        pega
    se trofeu
        pula
        interrompa
pula
'''

### Em python
'''
while true
    if bloco
        passo
    if buraco
        pula
    if moeda
        pega
    if trofeu
        pula
        break
pega
'''

### Brincando
'''
cont = 0
while True:
    print(cont, ' ', end='')
    cont += 1
print('acabou')
'''

'''
n = 0
s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
'''

'''
n = 0
s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
# print('A soma vale {}'.format(s))
'''

'''
nome = 'Jean'
idade = 33
print(f'O {nome} tem {idade} anos')
'''
