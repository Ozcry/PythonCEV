# Interactive Help
'''digitando help() no console python
Ou help(print)
ou print(input.__doc__)'''


# Docstrings
'''def contador(i, f, p):
    """==> Faz uma contagem e mostra na tela.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno"""
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')


contador(2, 10, 2)
help(contador)'''


# Parâmetros opcionais
'''def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()'''


# Escopo de Variáveis
'''def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')'''


'''def funcao():
    global n2
    n1 = 4
    n2 = 6
    print(f'N1 dentro vale {n1}')
    print(f'N2 dentro vale {n2}')


n1 = 2
n2 = 4
funcao()
print(f'N2 fora vale {n2}')
print(f'N1 fora vale {n1}')'''


# Retorno de Valores

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


resp = somar(3, 2, 5)
resp2 = somar(8, 4)
resp3 = somar()
print(f'Meus cálculos deram {resp}, {resp2}, e {resp3}')'''


# Brincando
'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''


'''def parouimpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if parouimpar(num):
    print('É par!')
else:
    print('Não é par!')'''
