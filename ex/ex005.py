### Crie um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.
n1 = int(input('Digite um numero: '))
cores = {'limpa': '\033[m', 'cinza': '\033[0;37m', 'ciano': '\033[0;36m', 'amarelo': '\033[0;33m'}
print('Seu numero {}{}{}, Antecessor {}{}{}, Sucessor {}{}{}.'.format(cores['cinza'], n1, cores['limpa'], cores['ciano'], (n1-1), cores['limpa'], cores['amarelo'], (n1+1), cores['limpa']))

### Outro metodo
#n1 = int(input('Digite um numero: '))
#a = n1 - 1
#s = n1 + 1
#print('Seu numero {}, Antecessor {}, Sucessor {}.'.format(n1, a, s))
