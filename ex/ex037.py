'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para Octal
- 3 para Hexadecimal'''
from time import sleep
print('\033[33m-=-\033[m' * 20)
print('\033[1;32mConversor de Decimal para Binário, Octal e Hexadecimal\033[m')
print('\033[33m-=-\033[m' * 20)
n1 = int(input('\033[34mDigite um número:\033[m '))
print('\033[33m-=-\033[m' * 20)
opcao = str(input('\033[35m1\033[m - Binário\n\033[36m2\033[m - Octal\n\033[31m3\033[m - Hexadecimal\n\033[1;34mEscolha uma opção:\033[m ')).strip()
print('\033[33m-=-\033[m' * 20)
print('\033[1;32mPROCESSANDO...\033[m')
sleep(2)
if opcao == '1':
    print('Seu número convertido para Binário é {}{}{}'.format('\033[35m', bin(n1)[2:], '\033[m'))
elif opcao == '2':
    print('Seu número convertido para Octal é {}{}{}'.format('\033[36m', oct(n1)[2:], '\033[m'))
elif opcao == '3':
    print('Seu número convertido para Hexadecimal é {}{}{}'.format('\033[31m', hex(n1)[2:], '\033[m'))
else:
    print('\033[1;31mOpção Invalida\033[m')
print('\033[33m-=-\033[m' * 20)
