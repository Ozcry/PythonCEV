'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''
homens = 0
adultos = 0
mulheres20 = 0
print('\033[1;33m-=\033[m' * 20)
while True:
    print('\033[1;32mCADASTRE UMA PESSOA\033[m')
    idade = int(input('\033[35mDigite sua idade:\033[m '))
    if idade > 18:
        adultos += 1
    sexo = str(input('\033[34mDigite seu sexo [M/F]:\033[m ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres20 += 1
    continuar = str(input('\033[37mContinuar [S/N]: \033[m')).strip().upper()[0]
    if continuar == 'N':
        print('\033[1;33m-=\033[m' * 20)
        break
    print('\033[1;33m-=\033[m' * 20)
print(f'\033[36m{adultos} pessoas tem mais de 18 anos\n{homens} homens foram cadastrados\n{mulheres20} mulheres tem menos de 20 anos\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
