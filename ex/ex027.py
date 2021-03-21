### Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
### ex: Ana Maria de Souza
### Primeiro = Ana
### Último = Souza
nome = str(input('\033[30mDigite seu nome:\033[m ')).strip()
nomed = nome.split()
print('\033[31mPrimeiro nome:\033[m {}{}{}'.format('\033[37m', nomed[0], '\033[m'))
print('\033[32mÚltimo nome:\033[m {}{}{}'.format('\033[33m', nomed[len(nomed) - 1], '\033[m'))
