### Crie um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('Sua media é \033[0;35m{:.1f}\033[m'.format((n1 + n2)/2))

### Outro metodo
#n1 = int(input('Digite a primeira nota: '))
#n2 = int(input('Digite a segunda nota: '))
#m = (n1 + n2)/2
#print('Sua media é {}.'.format(m))