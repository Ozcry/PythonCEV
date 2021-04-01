'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
contv = 0
maq = randint(0, 10)
print('\033[1;33m-=\033[m' * 20)
print('\033[1;37m------- Vamos jogar PAR ou Ímpar -------\033[m')
print('\033[1;33m-=\033[m' * 20)
while True:
    n1 = int(input('\033[35mDigite um valor de 0 a 10:\033[m '))
    pi = str(input('\033[36mPAR ou Ímpar [P/I]:\033[m ')).strip().upper()[0]
    print('\033[1;33m-=\033[m' * 20)
    if pi == 'I':
        soma = n1 + maq
        if soma % 2 == 0:
            print(f'\033[34mVocê jogou {n1} e o computador {maq}. Total: {soma}\033[m')
            print('\033[31mDeu PAR, Você perdeu!\033[m')
            print('\033[1;33m-=\033[m' * 20)
            break
        elif soma % 2 != 0:
            print(f'\033[34mVocê jogou {n1} e o computador {maq}. Total: {soma}\033[m')
            print('\033[32mDeu ÍMPAR, Você Ganhou!\033[m')
            print('\033[1;33m-=\033[m' * 20)
            contv += 1
    if pi == 'P':
        soma = n1 + maq
        if soma % 2 != 0:
            print(f'\033[34mVocê jogou {n1} e o computador {maq}. Total: {soma}\033[m')
            print('\033[31mDeu ÍMPAR, Você perdeu!\033[m')
            print('\033[1;33m-=\033[m' * 20)
            break
        elif soma % 2 == 0:
            print(f'\033[34mVocê jogou {n1} e o computador {maq}. Total: {soma}\033[m')
            print('\033[32mDeu PAR, Você Ganhou!\033[m')
            print('\033[1;33m-=\033[m' * 20)
            contv += 1
if contv == 1:
    print(f'\033[31mGame Over!! Você ganhou {contv} vez\033[m')
else:
    print(f'\033[31mGame Over!! Você ganhou {contv} vezes\033[m')
