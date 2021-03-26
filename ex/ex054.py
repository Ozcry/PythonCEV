'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantos pessoas ainda não atingiram a
maioridade e quantas já são maiores. Maior de idade com 21 anos
'''
adulto = 0
crianca = 0
print('\033[1;33m-=\033[m' * 20)
for c in range(0,7):
    idade = int(input('\033[31mDigite sua idade:\033[m '))
    if idade >= 21:
        adulto = adulto + 1
    else:
        crianca = crianca + 1
print('\033[1;33m-=\033[m' * 20)
if adulto != 0:
    print('{}{}{} \033[35mpessoas são maiores de idade.\033[m'.format('\033[36m', adulto, '\033[m'))
if crianca != 0:
    print('{}{}{} \033[34mpessoas são menores de idade.\033[m'.format('\033[37m', crianca, '\033[m'))
print('\033[1;33m-=\033[m' * 20)
