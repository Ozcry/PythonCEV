'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 18 <= idade < 65:
        return f'\033[35mCom {idade} anos o voto e obrigatório\033[m'
    elif 16 <= idade < 18 or idade >= 65:
        return f'\033[35mCom {idade} anos o voto e opcional\033[m'
    else:
        return f'\033[35mCom {idade} anos, não e necessario votar\033[m'


print('\033[1;33m-=\033[m' * 20)
print(voto(int(input('\033[34mEm que ano você nasceu?\033[m '))))
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
