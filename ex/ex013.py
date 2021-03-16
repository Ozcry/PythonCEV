### Crie um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
n1 = float(input('Digite o valor salario: '))
print('Seu antigo salário {:.2f}, seu novo salário {:.2f}'.format(n1, (n1 + (n1 * 15 / 100))))

###Outro metodo
#n1 = float(input('Digite o valor salario: '))
#d = n1 * 0.15
#f = n1 + d
#print('Seu antigo salário {:.2f}, seu novo salário {:.2f}'.format(n1, f))
