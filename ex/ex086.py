'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

### Outro metodo
'''
matrix = [[input('Digite um valor para [0,0]: '), input('Digite um valor para [0,1]: '), input('Digite um valor para [0,2]: ')],
          [input('Digite um valor para [1,0]: '), input('Digite um valor para [1,1]: '), input('Digite um valor para [1,2]: ')],
          [input('Digite um valor para [2,0]: '), input('Digite um valor para [2,1]: '), input('Digite um valor para [2,2]: ')]]
print('\033[1;33m-=\033[m' * 20)
print(f'[ {matrix[0][0]} ][ {matrix[0][1]} ][ {matrix[0][2]} ]\n[ {matrix[1][0]} ][ {matrix[1][1]} ][ {matrix[1][2]} ]\n'
      f'[ {matrix[2][0]} ][ {matrix[2][1]} ][ {matrix[2][2]} ]')
print('\033[1;33m-=\033[m' * 20)
print('FIM')
'''
