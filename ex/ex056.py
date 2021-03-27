'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
> A média de idade do grupo.
> Qual é o nome do homem mais velho.
> Quantas mulheres têm menos de 20 anos.
'''
mediai = 0
nomev = ''
idademaior = 0
mulheres20m = 0
print('\033[1;33m-=\033[m' * 20)
for c in range(1, 5):
    print('---------- {}ª PESSOA ----------'.format(c))
    nome = str(input('\033[37mDigite seu nome:\033[m ')).strip()
    idade = int(input('\033[31mDigite sua idade:\033[m '))
    sexo = int(input('\033[34m[\033[m\033[32m1\033[m\033[34m] - Masculino\033[m\n\033[34m[\033[m\033[33m2\033[m\033[34m] - Feminino\033[m\n\033[1;35mDigite aqui sua opção:\033[m '))
    print('\033[1;33m-=\033[m' * 20)
    mediai = mediai + idade
    if sexo == 2 and idade < 20:
        mulheres20m = mulheres20m + 1
    if idade > idademaior and sexo == 1:
        idademaior = idade
        nomev = nome
print('\033[36mA média de idade do grupo é\033[m {}{:.0f}{}'.format('\033[1;32m', mediai / 4, '\033[m'))
print('\033[36mO nome do homem mais velho é\033[m {}{}{}'.format('\033[1;32m', nomev.capitalize(), '\033[m'))
print('{}{}{} \033[36mmulheres têm menos de 20 anos\033[m'.format('\033[1;32m', mulheres20m, '\033[m'))
print('\033[1;33m-=\033[m' * 20)

### Outro metodo
'''
mediai = 0
nomev = ''
idademaior = 0
mulheres20m = 0
print('\033[1;33m-=\033[m' * 20)
for c in range(0,4):
    nome = str(input('\033[37mDigite seu nome:\033[m ')).strip()
    idade = int(input('\033[31mDigite sua idade:\033[m '))
    sexo = int(input('\033[34m[\033[m\033[32m1\033[m\033[34m] - Masculino\033[m\n\033[34m[\033[m\033[33m2\033[m\033[34m] - Feminino\033[m\n\033[1;35mDigite aqui sua opção:\033[m '))
    print('\033[1;33m-=\033[m' * 20)
    if sexo == 2 and idade < 20:
        mulheres20m = mulheres20m + 1
    if idade != 99999999999999999999999999:
        mediai = mediai + idade
    if idade > idademaior and sexo == 1:
        idademaior = idade
        nomev = nome
print('\033[36mA média de idade do grupo é\033[m {}{:.0f}{}'.format('\033[1;32m', mediai / 4, '\033[m'))
print('\033[36mO nome do homem mais velho é\033[m {}{}{}'.format('\033[1;32m', nomev.capitalize(), '\033[m'))
print('{}{}{} \033[36mmulheres têm menos de 20 anos\033[m'.format('\033[1;32m', mulheres20m, '\033[m'))
print('\033[1;33m-=\033[m' * 20)
'''
