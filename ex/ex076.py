'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular.'''
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('\033[1;33m-=\033[m' * 20)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for c in range(0, len(produtos)):
      if c % 2 == 0:
            print(f'{produtos[c]:.<30}', end='')
      else:
            print(f'R${produtos[c]:>7.2f}')
print('-' * 40)
print('\033[1;33m-=\033[m' * 20)

### Outro Metodo
'''
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 41)
print('           LISTAGEM DE PREÇOS')
print('-' * 41)
print(f'{produtos[0]}..........................R$   {produtos[1]:.2f}\n'
      f'{produtos[2]}.......................R$   {produtos[3]:.2f}\n'
      f'{produtos[4]}........................R$  {produtos[5]:.2f}\n'
      f'{produtos[6]}.........................R$  {produtos[7]:.2f}\n'
      f'{produtos[8]}...................R$   {produtos[9]:.2f}\n'
      f'{produtos[10]}.......................R$   {produtos[11]:.2f}\n'
      f'{produtos[12]}........................R$ {produtos[13]:.2f}\n'
      f'{produtos[14]}........................R$  {produtos[15]:.2f}\n'
      f'{produtos[16]}..........................R$  {produtos[17]:.2f}')
print('-' * 41)
'''
