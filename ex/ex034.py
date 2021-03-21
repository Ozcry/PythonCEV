### Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
### Para salários superiores a R$1.250,00, calcule um aumento de 10%.
### Para as inferiores ou iguais, o aumento é de 15%.
s = float(input('\033[31mDigite o valor do seu salário:\033[m '))
cores = {'limpa': '\033[m', 'ciano': '\033[36m', 'azul': '\033[34m'}
if s <= 1250:
    a1 = s + (s * 15 / 100)
    print('\033[32mSeu antigo salário R$\033[m{}{:.2f}{} \033[32mseu novo salário com aumento R$\033[m{}{:.2f}{}'.format(cores['ciano'], s, cores['limpa'], cores['azul'], a1, cores['limpa']))
else:
    a2 = s + (s * 10 / 100)
    print('\033[32mSeu antigo salário R$\033[m{}{:.2f}{} \033[32mseu novo salário com aumento R$\033[m{}{:.2f}{}'.format(cores['ciano'], s, cores['limpa'], cores['azul'], a2, cores['limpa']))
print('\033[33m--------------\033[m')
