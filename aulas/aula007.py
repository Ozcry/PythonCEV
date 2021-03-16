#  Operadores
#  +  Adição 5 + 2 == 7
#  -  Subtração 5 - 2 == 3
#  *  Multiplicação 5 * 2 == 10
#  /  Divisão 5 / 2 == 2.5
#  ** Potência 5 ** 2 == 25   ou  pow(4,3)
#  // Divisão Interna 5 // 2 == 2
#  %  Resto da Divisão 5 % 2 == 1
#  Raiz Quadrada   81**(1/2) == 9
#  Raiz Cúbica   127**(1/3) == 5.02

# Ordem de Precedência
# 1 -  ()
# 2 -  **
# 3 -  *   /   //   %
# 4 -  +    -

# Operações com strings
# 'Oi' + 'Olá' == 'OiOlá'
# 'Oi' * 5 == 'OiOiOiOiOi'
# '=' * 20 == '===================='

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n o produto é {},\n a divisão é {:.3f}'.format(s, m, d), end = ' >>> ')
print('a divisão inteira é {} e a potência é {}'.format(di, e))
