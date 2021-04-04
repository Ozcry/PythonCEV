'''
tuplas ()
listas []
'''

'''
valores = list(range(4, 11))
valores2 = [8, 2, 5, 4, 9, 3, 0]

valores2.sort() ---- Colocar em ordem
valores2.sort(reverse = True) ---- Ordem reversa

len(valores2)
'''

###
'''listas podem ser modificadas'''

### Adicionar coisas na lista
'''lanche.append('Cokkie') --- no final'''

'''lanche.insert(0.'Hotdog') --- em qualquer lugar'''

### Deletar coisas das listas
'''del lanche[3]'''

'''lanche.pop(3) ----- sem o parametro remove o ultimo objeto'''

'''lanche.remove('pizza') ---- remove pelo conteudo'''

'''if pizza in lanche:
    lanche.remove('pizza')'''

### Brincando

'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
#num.pop(2)
num.remove(2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')
'''

'''
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(valores)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}! ')

for c in valores:
    print(f'{c}... ', end='')
'''

'''
a = [2, 3, 4, 7]
b = a ------- B faz uma ligação com A
b = a[:] -------- B copia A
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''
