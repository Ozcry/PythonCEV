### Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
### Para salários superiores a R$1.250,00, calcule um aumento de 10%.
### Para as inferiores ou iguais, o aumento é de 15%.
s = float(input('Digite o valor do seu salário: '))
if s <= 1250:
    a1 = s + (s * 15 / 100)
    print('Seu antigo salário R${:.2f} seu novo salário com aumento R${:.2f}'.format(s, a1))
else:
    a2 = s + (s * 10 / 100)
    print('Seu antigo salário R${:.2f} seu novo salário com aumento R${:.2f}'.format(s, a2))
print('--------------')
