### Crie um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.
n1 = int(input('Digite um numero: '))
cores = {'limpa': '\033[m', 'branco': '\033[30m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'roxo': '\033[35m', 'ciano': '\033[36m', 'cinza': '\033[37m'}
print('\033[1;33;47m=-=\033[m' * 20)
print('Tabuada do {}{}{}\n{}{}{} * \033[30m1\033[m = {}{}{}\n{}{}{} * \033[31m2\033[m = {}{}{}\n{}{}{} * \033[32m3\033[m = {}{}{}\n{}{}{} * \033[33m4\033[m = {}{}{}\n{}{}{} * \033[34m5\033[m = {}{}{}\n{}{}{} * \033[35m6\033[m = {}{}{}\n{}{}{} * \033[36m7\033[m = {}{}{}\n{}{}{} * \033[37m8\033[m = {}{}{}\n{}{}{} * \033[30m9\033[m = {}{}{}\n{}{}{} * \033[31m10\033[m = {}{}{}'
      .format(cores['cinza'], n1, cores['limpa'], cores['ciano'], n1, cores['limpa'], cores['roxo'], (n1 * 1), cores['limpa'], cores['azul'], n1, cores['limpa'], cores['amarelo'], (n1 * 2), cores['limpa'], cores['verde'], n1, cores['limpa'], cores['vermelho'], (n1 * 3), cores['limpa'], cores['branco'], n1, cores['limpa'], cores['cinza'], (n1 * 4), cores['limpa'], cores['ciano'], n1, cores['limpa'], cores['roxo'], (n1 * 5), cores['limpa'], cores['azul'], n1, cores['limpa'], cores['amarelo'], (n1 * 6), cores['limpa'], cores['verde'], n1, cores['limpa'], cores['vermelho'], (n1 * 7), cores['limpa'], cores['branco'], n1, cores['limpa'], cores['cinza'], (n1 * 8), cores['limpa'], cores['ciano'], n1, cores['limpa'], cores['roxo'], (n1 * 9), cores['limpa'], cores['azul'], n1, cores['limpa'], cores['amarelo'], (n1 * 10), cores['limpa']))
print('\033[1;33;47m=-=\033[m' * 20)

### Outro metodo
#n1 = int(input('Digite um numero: '))
#a = n1 * 1
#b = n1 * 2
#c = n1 * 3
#d = n1 * 4
#e = n1 * 5
#f = n1 * 6
#g = n1 * 7
#h = n1 * 8
#i = n1 * 9
#j = n1 * 10
#print('Tabuada do {}\n{} * 1 = {}\n{} * 2 = {}\n{} * 3 = {}\n{} * 4 = {}\n{} * 5 = {}\n{} * 6 = {}\n{} * 7 = {}\n{} * 8 = {}\n{} * 9 = {}\n{} * 10 = {}'.format(n1, n1, a, n1, b, n1, c, n1, d, n1, e, n1, f, n1, g, n1, h, n1, i, n1, j))