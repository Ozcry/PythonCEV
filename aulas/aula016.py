### Variaveis compostas TUPLAS
'''print(lanche[2])'''
'''print(lanche[0:2])'''
'''print(lanche[1:])'''
'''print(lanche[-1])'''
'''len(lanche)'''
'''for c in lanche:
    print(c)'''

###
''''As tuplas são IMUTÁVEIS'''

### Brincando
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudím')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b +a
pessoa = ('Jean', 23, 'M', 65.5)

print(lanche[1])

'''for c in lanche:
    print(f'Eu vou comer {c}')'''

'''for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')'''

'''for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')'''

'''print(sorted(lanche))'''

'''print(c.count(5))'''

'''print(c.index(5, 1))'''

'''del pessoa'''
