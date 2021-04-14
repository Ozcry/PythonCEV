'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.'''


def ficha(nome='<desconhecido>', gols='0'):
    print('\033[1;33m-=\033[m' * 20)
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    return f'\033[36mO jogador {nome} fez {gols} gol(s) no campeonato.\033[m'


print('\033[1;33m-=\033[m' * 20)
print(ficha(str(input('\033[34mNome do jogador:\033[m ')).strip().capitalize(), str(input('\033[35mNúmeros de gols:\033[m '))))
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')