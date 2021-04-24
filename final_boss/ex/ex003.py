'''-> Crie um programa que leia dois números e mostre a soma entre eles.'''
from final_boss.modulos import mat, texto
texto.linha(33)
n1 = mat.leianumfi('Digite um número: ', 35)
n2 = mat.leianumfi('Digite outro: ', 36)
texto.linha(33)
texto.escreva(f'A soma entre {n1} e {n2} vale {mat.somanum(n1, n2)}', 34)
texto.linha(33)
texto.escreva('FIM', 32, 1)
