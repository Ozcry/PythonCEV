### Crie um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
n1 = float(input('Digite o valor salario: '))
print('Seu antigo salário {}{:.2f}{}, seu novo salário {}{:.2f}{}'.format('\033[0;34m', n1, '\033[m', '\033[36m', (n1 + (n1 * 15 / 100)), '\033[m'))

###Outro metodo
#n1 = float(input('Digite o valor salario: '))
#d = n1 * 0.15
#f = n1 + d
#print('Seu antigo salário {:.2f}, seu novo salário {:.2f}'.format(n1, f))
