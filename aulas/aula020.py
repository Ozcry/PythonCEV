'''
def mostralinha():
    print('\033[1;33m-=\033[m' * 20)


# Programa principal
mostralinha()
print('teste')
mostralinha()
print('teste')
mostralinha()
print('jean lucas')
mostralinha()
'''


'''
def mensagem(msg):
    print('\033[1;33m-=\033[m' * 20)
    print(msg)
    print('\033[1;33m-=\033[m' * 20)


# Programa principal
mensagem('Sistema de alunos')
mensagem('teste')
mensagem('jean lucas')
'''

# Brincando


'''
def lin():
    print('\033[1;33m-=\033[m' * 20)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa principal
soma(4, 5)
lin()
soma(8, 9)
lin()
soma(2, 1)
lin()
soma(a=4, b=4)
lin()
soma(b=4, a=3)
'''


'''
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    """for valor in num:
        print(valor, end=' ')"""
    print('FIM!')


# Programa principal
contador(5, 7, 3, 1, 4)
contador(4, 4, 7)
contador(2)
'''


'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Programa principal
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
'''


'''
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


# Programa principal
soma(5, 2)
soma(2, 9, 4)
soma(1, 3, 7, 4, 9, 0)
'''
