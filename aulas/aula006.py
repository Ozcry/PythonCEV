# int = 7, -4, 0, 9875
# float = 4.5, 0.076, -15.223, 7.0
# bool = True, False
# str = 'Olá' '7.5' ''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
#print('A soma entre',n1,'e',n2,'vale',s) velho metodo
print('A soma entre{} e {} vale {}'.format(n1, n2, s))