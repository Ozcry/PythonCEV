'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o compeonato.'''
print('\033[1;33m-=\033[m' * 20)
jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador? ')).capitalize().strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1, partidas + 1):
    n1 = int(input(f'Quantos gols na partida {c}? '))
    gols.append(n1)
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('\033[1;33m-=\033[m' * 20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, c in enumerate(jogador['gols']):
    print(f'=> Na partida {i + 1}, fez {c} gols.')
print(f'Foi um total de {jogador["total"]}.')
print('\033[1;33m-=\033[m' * 20)
print('FIM')
