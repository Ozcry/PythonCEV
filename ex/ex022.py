### Crie um programa que leia o nome completo de uma pessoa e mostre:
### > O nome com todas as letras maiúsculas.
### > O nome com todas minúsculas.
### > Quantas letras ao t-odo (sem considerar espaços).
### > Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome: ')).strip()
nome2 = nome.split()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print(len(nome2[0]))
