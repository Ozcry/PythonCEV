'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida:
- Média abaixo de 5.0:
REPROVADO
- Média entre 5.0 e 6.9:
RECUPERAÇÃO
- Média 7.0 ou superior:
APROVADO'''
print('\033[35m=-=\033[m' * 20)
nota1 = float(input('\033[33mDigite a primeira nota:\033[m '))
nota2 = float(input('\033[33mDigite a segunda nota:\033[m '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('\033[31mREPROVADO!!\033[m')
elif media >= 7.0:
    print('\033[32mAPROVADO!!\033[m')
else:
    print('\033[36mRECUPERAÇÃO!!\033[m')
print('\033[35m=-=\033[m' * 20)
