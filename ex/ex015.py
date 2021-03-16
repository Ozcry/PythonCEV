### Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
n1 = float(input('Quantidade de Km percorridos: '))
n2 = int(input('Quantidade de dias: '))
print('Valor pelos Km percorridos R${:.2f}\nValor pela Quantidade de dias R${:.2f}\nValor Total: R${:.2f}'.format((n1 * 0.15),(n2 * 60),(n1 * 0.15 + n2 * 60)))
