'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da pragressão usando a estrutura while.'''
print('\033[1;33m-=\033[m' * 20)
n1 = int(input('\033[31mDigite o primeiro termo:\033[m '))
pa = int(input('\033[32mDigite a razão da PA:\033[m '))
print('\033[1;33m-=\033[m' * 20)
print('\033[34mOs Próximos 10 termos da sua PA são:\033[m')
resposta = n1
while resposta < n1 + pa * 10:
    resposta += pa
    print(resposta, '', end='')
print('\033[35mFIM\033[m')
print('\033[1;33m-=\033[m' * 20)
