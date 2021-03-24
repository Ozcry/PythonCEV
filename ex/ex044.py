'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
de pagamento:
- Á vista dinheiro/cheque: 10% de desconto
- Á vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''
pp = float(input('\033[1;32mDigite o valor do produto:\033[m '))
print('\033[33;47m-=-\033[m' * 20)
print('\033[1;32mEscolha a forma de pagamento\033[m')
cp = int(input('\033[36m1\033[m - Á vista ou cheque\n\033[35m2\033[m - Á vista no cartão\n\033[34m3\033[m - Em até 2x no cartão\n\033[33m4\033[m - 3x ou mais no cartão\n\033[1;32mDigite aqui sua opção:\033[m '))
print('\033[33;47m-=-\033[m' * 20)
if cp == 1:
    print('Escolhendo essa opção de pagamento, o produto que custa R$\033[32m{:.2f}\033[m, custara R$\033[32m{:.2f}\033[m'.format(pp, pp - (pp * 10 / 100)))
elif cp == 2:
    print('Escolhendo essa opção de pagamento, o produto que custa R$\033[32m{:.2f}\033[m, custara R$\033[32m{:.2f}\033[m'.format(pp, pp - (pp * 5 / 100)))
elif cp == 3:
    print('Escolhendo essa opção de pagamento, o produto que custa R$\033[32m{:.2f}\033[m, sairá pelo preço normal.'.format(pp,))
elif cp == 4:
    print('Escolhendo essa opção de pagamento, o produto que custa R$\033[32m{:.2f}\033[m, custara R$\033[32m{:.2f}\033[m com 20% de juros'.format(pp, pp + (pp * 20 / 100)))
else:
    print('\033[1;31mOpção invalida\033[m')
print('\033[33;47m-=-\033[m' * 20)
