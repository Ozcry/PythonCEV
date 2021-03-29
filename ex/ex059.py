'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
print('\033[1;33m-=\033[m' * 20)
n1 = float(input('\033[34mDigite um número:\033[m '))
n2 = float(input('\033[35mDigite outro número:\033[m '))
print('\033[1;33m-=\033[m' * 20)
sair = 0
while sair == 0:
    escolha = int(input('[\033[32m1\033[m] somar\n[\033[34m2\033[m] multiplicar\n[\033[35m3\033[m] maior\n[\033[36m4\033[m] novos números\n[\033[37m5\033[m] sair do programa\n\033[31mDigite aqui sua opção:\033[m '))
    print('\033[1;33m-=\033[m' * 20)
    if escolha == 1:
        print('A soma entre {}{:.1f}{} e {}{:.1f}{} é {}{:.1f}{}'.format('\033[36m', n1, '\033[m', '\033[35m', n2, '\033[m', '\033[34m', n1 + n2, '\033[m'))
        print('\033[1;33m-=\033[m' * 20)
    elif escolha == 2:
        print('O produto entre {}{:.1f}{} e {}{:.1f}{} é {}{:.1f}{}'.format('\033[36m', n1, '\033[m', '\033[35m', n2, '\033[m', '\033[34m', n1 * n2, '\033[m'))
        print('\033[1;33m-=\033[m' * 20)
    elif escolha == 3:
        if n1 > n2:
            print('{}{:.1f}{} é maior que {}{:.1f}{}'.format('\033[36m', n1, '\033[m', '\033[35m', n2, '\033[m'))
            print('\033[1;33m-=\033[m' * 20)
        elif n1 == n2:
            print('Os números são iguais')
            print('\033[1;33m-=\033[m' * 20)
        else:
            print('{}{:.1f}{} é maior que {}{:.1f}{}'.format('\033[35m', n2, '\033[m', '\033[36m', n1, '\033[m'))
            print('\033[1;33m-=\033[m' * 20)
    elif escolha == 4:
        n3 = float(input('\033[34mDigite um número:\033[m '))
        n1 = n3
        n4 = float(input('\033[35mDigite outro número:\033[m '))
        n2 = n4
        print('\033[1;33m-=\033[m' * 20)
    elif escolha == 5:
        sair +=1
    else:
        print('\033[1;31mOPÇÃO INVALIDA, tente novamente!\033[m')
        print('\033[1;33m-=\033[m' * 20)
print('\033[1;30mFIM\033[m')
print('\033[1;33m-=\033[m' * 20)
