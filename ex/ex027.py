### Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
### ex: Ana Maria de Souza
### Primeiro = Ana
### Último = Souza
nome = str(input('digite seu nome: ')).strip()
nomed = nome.split()
print('Primeiro nome: {}'.format(nomed[0]))
print('Último nome: {}'.format(nomed[len(nomed) - 1]))
