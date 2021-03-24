'''Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import choice
from time import sleep
print('\033[33m-=-\033[m' * 20)
print('\033[1;36mVamos jogar Jokenpô\033[m')
print('\033[33m-=-\033[m' * 20)
opj = str(input('Escolha uma opção \033[1;35mPedra\033[m, \033[1;34mPapel\033[m ou \033[1;33mTesoura\033[m: ')).strip().upper()
maqop = 'Pedra', 'Papel', 'Tesoura'
maquina = choice(maqop)
print('\033[1;32mPROCESSANDO...\033[m')
sleep(2)
if opj == 'PEDRA' and maquina == 'Pedra':
    print('\033[1;36mEmpate\033[m, eu também escolhi \033[35mPedra\033[m')
elif opj == 'PEDRA' and maquina == 'Papel':
    print('\033[1;31mVocê perdeu\033[m, eu escolhi \033[34mPapel\033[m')
elif opj == 'PEDRA' and maquina == 'Tesoura':
    print('\033[1;32mVocê ganhou\033[m, eu escolhi \033[33mTesoura\033[m')
elif opj == 'PAPEL' and maquina == 'Pedra':
    print('\033[1;32mVocê ganhou\033[m, eu escolhi \033[35mPedra\033[m')
elif opj == 'PAPEL' and maquina == 'Papel':
    print('\033[1;36mEmpate\033[m, eu também escolhi \033[34mPapel\033[m')
elif opj == 'PAPEL' and maquina == 'Tesoura':
    print('\033[1;31mVocê perdeu\033[m, eu escolhi \033[33mTesoura\033[m')
elif opj == 'TESOURA' and maquina == 'Pedra':
    print('\033[1;31mVocê perdeu\033[m, eu escolhi \033[35mPedra\033[m')
elif opj == 'TESOURA' and maquina == 'Papel':
    print('\033[1;32mVocê ganhou\033[m, eu escolhi \033[34mPapel\033[m')
elif opj == 'TESOURA' and maquina == 'Tesoura':
    print('\033[1;36mEmpate\033[m, eu também escolhi \033[33mTesoura\033[m')
else:
    print('\033[1;31mOPÇÃO INVALIDA\033[m')
print('\033[33m-=-\033[m' * 20)
