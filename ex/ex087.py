'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
for l in range(0, 3):
    scol += matriz[l][2]
for l in range(0, 3):
    if l == 0:
        mai = matriz[1][l]
    elif matriz[1][l] > mai:
        mai = matriz[1][l]
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
print(f'A soma dos valores da terceira coluna é {scol}')
print(f'O maior valor da segunda linha é {mai}')

###Outro metodo
'''
print('\033[1;33m-=\033[m' * 20)
matrix = [[int(input('Digite um valor para [0,0]: ')), int(input('Digite um valor para [0,1]: ')), int(input('Digite um valor para [0,2]: '))],
          [int(input('Digite um valor para [1,0]: ')), int(input('Digite um valor para [1,1]: ')), int(input('Digite um valor para [1,2]: '))],
          [int(input('Digite um valor para [2,0]: ')), int(input('Digite um valor para [2,1]: ')), int(input('Digite um valor para [2,2]: '))]]
soma = 0
for c in matrix:
    for v in c:
        if v % 2 == 0:
            soma += v
print('\033[1;33m-=\033[m' * 20)
print(f'[ {matrix[0][0]} ][ {matrix[0][1]} ][ {matrix[0][2]} ]\n[ {matrix[1][0]} ][ {matrix[1][1]} ][ {matrix[1][2]} ]\n'
      f'[ {matrix[2][0]} ][ {matrix[2][1]} ][ {matrix[2][2]} ]')
print('\033[1;33m-=\033[m' * 20)
print(f'O maior valor da segunda linha é {max(matrix[1])}')
print(f'A soma dos valores da terceira coluna é {matrix[0][2] + matrix[1][2] + matrix[2][2]}')
print(f'A soma dos valores pares é {soma}')
print('\033[1;33m-=\033[m' * 20)
print('FIM')
'''
