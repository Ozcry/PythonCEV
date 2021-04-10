'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o compeonato.'''
print('\033[1;33m-=\033[m' * 20)
jogador = {}
gols = []
jogador['nome'] = str(input('\033[31mNome do jogador? \033[m')).capitalize().strip()
partidas = int(input(f'\033[32mQuantas partidas {jogador["nome"]} jogou? \033[m'))
for c in range(1, partidas + 1):
    gols.append(int(input(f'\033[34m => Quantos gols na partida {c}? \033[m')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('\033[1;33m-=\033[m' * 20)
print(f'\033[35mO jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.\033[m')
for i, c in enumerate(jogador['gols']):
    print(f'\033[36m -> Na partida {i + 1}, fez {c} gols.\033[m')
print(f'\033[37mFoi um total de {jogador["total"]}.\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
