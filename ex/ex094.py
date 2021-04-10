'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) uma lista com todas as pessoas com idade acima da média'''
print('\033[1;33m-=\033[m' * 20)
dados = {}
lista = []
mulheres = []
soma = 0
while True:
    aux3 = str(input('\033[31mDigite seu nome: \033[m')).strip().capitalize()
    dados['nome'] = aux3
    aux = ' '
    while aux not in 'MF':
        aux = str(input('\033[32mSexo [M/F]:\033[m ')).strip().upper()[0]
    dados['sexo'] = aux
    if aux == 'F':
        mulheres.append(aux3)
    aux2 = int(input('\033[33mDigite sua idade:\033[m '))
    soma += aux2
    dados['idade'] = aux2
    lista.append(dados.copy())
    dados.clear()
    sair = ' '
    while sair not in 'SN':
        sair = str(input('\033[34mContinuar [S/N]:\033[m ')).strip().upper()[0]
    print('\033[1;33m-=\033[m' * 20)
    if sair == 'N':
        break
media = soma / len(lista)
print(f'\033[35m-> Ao todo temos {len(lista)} pessoas cadastradas.\033[m')
print(f'\033[36m-> A média de idade é {media:.0f}\033[m')
print('\033[37m-> As mulheres cadastradas foram \033[m', end='')
for c in mulheres:
    print(c, end=' ')
print()
print('\033[31m-> Lista das pessoas que estão acima da média:\033[m')
for c in lista:
    if c['idade'] > media:
        print(f'\033[34m    nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]};\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
