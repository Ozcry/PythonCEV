'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print('\033[1;33m-=\033[m' * 20)
while True:
    n1 = int(input('\033[36mDigite um número entre 0 e 20:\033[m '))
    while n1 not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
        n1 = int(input('\033[31mTente novamente, digite um número entre 0 e 20:\033[m '))
    print(f'\033[35mVocê digitou o número {n1} que por extenso é {contagem[n1]}\033[m')
    print('\033[1;33m-=\033[m' * 20)
    sair = ' '
    while sair != 'S' or sair != 'N':
        sair = str(input('\033[34mContinuar [S/N]:\033[m ')).strip().upper()[0]
        print('\033[1;33m-=\033[m' * 20)
        if sair == 'S':
            break
        elif sair == 'N':
            break
    if sair == 'N':
        break
print('\033[1;32mFIM\033[m')
