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
    aux3 = str(input('Digite seu nome: ')).strip().capitalize()
    dados['nome'] = aux3
    aux = ' '
    while aux not in 'MF':
        aux = str(input('Sexo [M/F]: ')).strip().upper()[0]
    dados['sexo'] = aux
    if aux == 'F':
        mulheres.append(aux3)
    aux2 = int(input('Digite sua idade: '))
    soma += aux2
    dados['idade'] = aux2
    lista.append(dados.copy())
    dados.clear()
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Continuar [S/N]: ')).strip().upper()[0]
    print('\033[1;33m-=\033[m' * 20)
    if sair == 'N':
        break
media = soma / len(lista)
print(f'-> Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'-> A média de idade é {media:.0f}')
print('-> As mulheres cadastradas foram ', end='')
for c in mulheres:
    print(c, end=' ')
print()
print('-> Lista das pessoas que estão acima da média:')
for c in lista:
    if c['idade'] > media:
        print(f'    nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]};')
print('\033[1;33m-=\033[m' * 20)
print('FIM')
