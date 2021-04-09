'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
conteúdo da estrutura na tela.'''
print('\033[1;33m-=\033[m' * 20)
dic = {}
dic['nome'] = str(input('Digite seu nome: '))
dic['média'] = float(input('Digite sua média: '))
if dic['média'] < 7:
    dic['situação'] = 'Reprovado'
else:
    dic['situação'] = 'Aprovado'
print('\033[1;33m-=\033[m' * 20)
print(f'-> O nome é {dic["nome"]}')
print(f'-> Média e igual a {dic["média"]}')
print(f'-> Situação e igual a {dic["situação"]}')
print('\033[1;33m-=\033[m' * 20)
print('FIM')
