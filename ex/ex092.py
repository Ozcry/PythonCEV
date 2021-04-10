'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a CTPS for diferente de zero, o dicionário recebera também o ano de contratação e o salário. calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
print('\033[1;33m-=\033[m' * 20)
from datetime import date
cadastro = {}
cadastro['nome'] = str(input('\033[31mDigite seu nome:\033[m ')).capitalize().strip()
ano = int(input('\033[32mAno de nascimento: \033[m'))
cadastro['idade'] = date.today().year - ano
cadastro['cdt'] = int(input('\033[34mCarteira de Trabalho (0 não tem):\033[m '))
if cadastro['cdt'] == 0:
    print('\033[1;33m-=\033[m' * 20)
    print(f'\033[36m  -> Nome: {cadastro["nome"]}\033[m')
    print(f'\033[37m  -> Idade: {cadastro["idade"]}\033[m')
    print('\033[30m  -> CTPS: Não possui\033[m')
elif cadastro['cdt'] != 0:
    cadastro['adc'] = int(input('\033[33mAno de Contratação:\033[m '))
    cadastro['salario'] = float(input('\033[35mSalário: R$\033[m'))
    cadastro['aposentadoria'] = (cadastro['adc'] - ano) + 35
    print('\033[1;33m-=\033[m' * 20)
    print(f'\033[31m  -> Nome: {cadastro["nome"]}\033[m')
    print(f'\033[32m  -> Idade: {cadastro["idade"]}\033[m')
    print(f'\033[33m  -> CTPS: {cadastro["cdt"]}\033[m')
    print(f'\033[34m  -> Ano de contratação: {cadastro["adc"]}\033[m')
    print(f'\033[35m  -> Salário R${cadastro["salario"]:.2f}\033[m')
    print(f'\033[36m  -> Idade na aposentadoria: {cadastro["aposentadoria"]}\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
