'''
Crie um programa que leia uma frase qualquer e diga se ela é um políndromo, desconsiderando os espaços.
Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA
'''
frase = str(input('Digite sua frase: ')).strip()
dividido = frase.split()
junto = ''.join(dividido)
numero = int(junto)
'''frase2 = int(frase)
for c in range(int(frase2), -1):
    if frase2 == c:
        print('Sua frase é um políndromo')
    if frase2 != c:
        print('Sua frase nãe é um políndromo')'''
'''.replace(" ", "")'''