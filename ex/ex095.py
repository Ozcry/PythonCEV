'''Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.'''
print('\033[1;33m-=\033[m' * 30)
time = []
gols = []
jogador = {}
while True:
    jogador['nome'] = str(input('\033[31mNome do jogador? \033[m')).capitalize()
    partidas = int(input(f'\033[32mQuantas partidas {jogador["nome"]} jogou?\033[m '))
    for c in range(1, partidas + 1):
        n1 = int(input(f'  \033[34m-> Quantos gols na partida {c}? \033[m'))
        gols.append(n1)
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    sair = ' '
    while sair not in 'SN':
        sair = str(input('\033[35mContinuar [S/N]:\033[m ')).strip().upper()[0]
    print('\033[1;33m-=\033[m' * 30)
    if sair == 'N':
        break
print(f'\033[36m{"cod":<4}{"nome":<15}{"gols":<25}{"total":<5}\033[m')
print('-' * 50)
for i, c in enumerate(time):
    print(f'\033[37m{i + 1:<4}{c["nome"]:<15}{str(c["gols"]):<25}{c["total"]}\033[m')
print('\033[1;33m-=\033[m' * 30)
while True:
    dados = 999
    while dados > len(time) or dados < 1:
        dados = int(input('\033[31mMostrar dados de qual jogador?\033[m '))
    for i, c in enumerate(time):
        if dados == i + 1:
            print(f'\033[32m --> LEVANTAMENTO DO JOGADOR {c["nome"]}:\033[m')
            for hi, ce in enumerate(c['gols']):
                print(f'\033[34m      No jogo {hi + 1}, fez {ce} gols.\033[m')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('\033[35mContinuar[S/N]: \033[m')).strip().upper()[0]
    print('\033[1;33m-=\033[m' * 30)
    if sair == 'N':
        break
print('\033[1;32mFIM\033[m')
