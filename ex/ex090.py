'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
conteúdo da estrutura na tela.'''
print('\033[1;33m-=\033[m' * 20)
dic = {}
dic['nome'] = str(input('\033[31mDigite seu nome:\033[m '))
dic['média'] = float(input('\033[34mDigite sua média:\033[m '))
if dic['média'] < 7:
    dic['situação'] = 'Reprovado'
else:
    dic['situação'] = 'Aprovado'
print('\033[1;33m-=\033[m' * 20)
print(f'\033[35m-> O nome é {dic["nome"]}\033[m')
print(f'\033[36m-> Média e igual a {dic["média"]}\033[m')
print(f'\033[37m-> Situação e igual a {dic["situação"]}\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
