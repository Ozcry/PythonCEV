'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
A) Apenas os 5 primeiros colocados
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time da Chapecoense.'''
tabela = ('Flamengo', 'Internacional', 'Atlético Mineiro', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthias', 'Atlético Goianiense', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print('\033[1;33m-=\033[m' * 20)
print(f'\033[34mTabela Brasileirão 2020 \033[m{tabela}')
print('\033[1;33m-=\033[m' * 20)
print(f'\033[35mPrimeiros 5 colocados \033[m{tabela[:5]}')
print('\033[1;33m-=\033[m' * 20)
print(f'\033[36mÚltimos 4 colocados\033[m {tabela[-5:]}')
print('\033[1;33m-=\033[m' * 20)
print(f'\033[37mTimes em ordem alfabética \033[m{sorted(tabela)}')
print('\033[1;33m-=\033[m' * 20)
if 'Chapecoense' not in tabela:
    print('\033[31mO time da Chapecoense não está disputando o campeonato.\033[m')
    print('\033[1;33m-=\033[m' * 20)
posicaog = tabela.index('Grêmio') + 1
print(f'\033[33mO time do Grêmio esta na {posicaog}ª posição\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
