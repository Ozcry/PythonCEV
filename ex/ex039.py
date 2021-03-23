'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
print('\033[35m=-=\033[m' * 20)
anon = int(input('\033[33mDigite o ano em que você nasceu:\033[m '))
if date.today().year - anon < 18:
    print('Você ainda tera que se alistar, faltam \033[34m{}\033[m anos.'.format(anon + 18 - date.today().year))
elif date.today().year == anon + 18:
    print('Você tem que se alistar esse ano! Não se esqueça.')
else:
    print('Você ja passou do tempo de alistamento, foi a \033[34m{}\033[m anos atrás.'.format(date.today().year - (anon + 18)))
print('\033[35m=-=\033[m' * 20)
