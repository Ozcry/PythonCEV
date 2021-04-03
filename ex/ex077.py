'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.'''
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
print('\033[1;33m-=\033[m' * 20)
for c in palavras:
    print(f'\n\033[35mNa palavra\033[m {c} \033[35mtemos\033[m ', end='')
    for l in c:
        if l in 'AEIOU':
            print(f'{l.lower()} ', end='')
print('\n')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
