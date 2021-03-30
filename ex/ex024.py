'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".'''
cidade = str(input('\033[35m Digite o nome da cidade:\033[m ')).strip().upper().split()
print('\033[36m', 'SANTO' in cidade[0], '\033[m')
