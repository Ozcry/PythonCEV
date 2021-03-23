'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''
valor = float(input('\033[33mDigite o valor da casa:\033[m '))
salario = float(input('\033[33mDigite o valor do seu salário:\033[m '))
anos = int(input('\033[33mEm quantos anos planeja pagar?\033[m '))

if valor / (anos * 12) < (salario * 30) / 100:
    print('Enpréstimo \033[32mAPROVADO\033[m')
    print('Sua prestação mensal sera de R${:.2f}'.format(valor / (anos * 12)))

else:
    print('Empréstimo \033[31mNÃO APROVADO\033[m')
