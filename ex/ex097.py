'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
Ex:. escreva(Olá, Mundo!)
Saída:. -----------
        Olá, Mundo!
        -----------
'''


def escreva(texto):
    tam = len(texto) + 4
    print('\033[35m~\033[m' * tam)
    print(f'\033[34m  {texto}\033[m')
    print('\033[35m~\033[m' * tam)


escreva('tamanho adaptável')
escreva('Faça')
escreva('programa')
escreva('um')
escreva('um programa que tenha uma')
