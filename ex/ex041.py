'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 18 anos: Junior
- Até 20 anos: Sênior
- Acima: Master'''
from datetime import date
ano = int(input('\033[33mDigite o seu ano de nascimento:\033[m '))
if date.today().year - ano <= 9:
    print('\033[31mSua categoria é Mirim!\033[m')
elif 9 < date.today().year - ano <= 14:
    print('\033[32mSua categoria é Infantil!\033[m')
elif 14 < date.today().year - ano <=18:
    print('\033[34mSua categoria é Junior!\033[m')
elif 18 < date.today().year - ano <= 20:
    print('\033[35mSua categoria é Sênior!\033[m')
else:
    print('\033[36mSua categoria é Master!\033[m')
