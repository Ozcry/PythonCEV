### ANSI
'''
\033[style; text; backgroundm
\033[0;33;44m

style - 0 = faz nada, 1 = negrito, 4 = subliando, 7 = inverter configurações
text - 30 = branco, 31 = vermelho, 32 = verde, 33 = amarelo, 34 = azul, 35 = roxo, 36 = ciano, 37 = cinza
background - 40 = branco, 41 = vermelho, 42 = verde, 43 = amarelo, 44 = azul, 45 = roxo, 46 = ciano, 47 = cinza
'''

'''
\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m
\033[7;30m
'''

### Brincando
'''
print('\033[7;33;44mOlá Mundo!\033[m')
'''

'''
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!'.format(a, b))
'''

'''
nome = 'Jean'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))
'''

'''
nome = 'Jean'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer,{}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))
'''
