''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
print('\033[1;33m-=\033[m' * 20)
sexo = ''
while sexo == '':
    sex = str(input('\033[36mInforme seu sexo [M/F]:\033[m ')).upper().strip()[0]
    if sex == 'M' or sex == 'F':
        sexo = sex
    else:
        print('\033[1;31mOPÇÃO INVALIDA, tente novamente!!!\033[m')
        print('\033[32m-=\033[m' * 20)
print('\033[1;33m-=\033[m' * 20)
if sexo == 'M':
    print('\033[37mSeu sexo é masculino\033[m')
elif sexo == 'F':
    print('\033[35mSeu sexo é feminino\033[m')
print('\033[34m--------FIM--------\033[m')
