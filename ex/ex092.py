'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a CTPS for diferente de zero, o dicionário recebera também o ano de contratação e o salário. calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
print('\033[1;33m-=\033[m' * 20)
from datetime import date
cadastro = {}
cadastro['nome'] = str(input('Digite seu nome: ')).capitalize().strip()
ano = int(input('Ano de nascimento: '))
cadastro['idade'] = date.today().year - ano
cadastro['cdt'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['cdt'] == 0:
    print('\033[1;33m-=\033[m' * 20)
    print(f'  -> Nome: {cadastro["nome"]}')
    print(f'  -> Idade: {cadastro["idade"]}')
    print('  -> CTPS: Não possui')
elif cadastro['cdt'] != 0:
    cadastro['adc'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['adc'] + 35
    print('\033[1;33m-=\033[m' * 20)
    print(f'  -> Nome: {cadastro["nome"]}')
    print(f'  -> Idade: {cadastro["idade"]}')
    print(f'  -> CTPS: {cadastro["cdt"]}')
    print(f'  -> Ano de contratação: {cadastro["adc"]}')
    print(f'  -> Salário R${cadastro["salario"]:.2f}')
    print(f'  -> Ano de aposentadoria: {cadastro["aposentadoria"]}')
print('\033[1;33m-=\033[m' * 20)
print('FIM')
