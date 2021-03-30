'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.'''
print('\033[1;33m-=\033[m' * 20)
n1 = int(input('\033[31mDigite o primeiro termo:\033[m '))
pa = int(input('\033[32mDigite a razão da PA:\033[m '))
termo = n1
contador = 1
total = 0
mais = 10
print('\033[1;33m-=\033[m' * 20)
print('\033[34mOs Próximos 10 termos da sua PA são:\033[m')
while mais != 0:
    total = total + mais
    while contador <= total:
        print(termo)
        termo += pa
        contador += 1
    print('\033[1;33m-=\033[m' * 20)
    mais = int(input('\033[36mDeseja ver mais quantos termos? digite [0] para sair: \033[m'))
    print('\033[1;33m-=\033[m' * 20)
    if mais != 0:
        print('\033[34mOs Próximos {} termos da sua PA são:\033[m'.format(mais))
print('\033[35mFIM\033[m')
