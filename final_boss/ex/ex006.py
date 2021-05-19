'''-> Crie um programa que leia um numero e mostre o seu dobro, triplo e raiz quadrada.'''
from final_boss.modulos import mat, texto

texto.linha(33, 1)
n1 = mat.leiaint('Digite um número: ', 35)
texto.linha(sty=1)
mat.dobro(n1, 34)
mat.triplo(n1, 31)
mat.raizqua(n1, 36)
texto.linha(33, 1)
texto.escreva('FIM', 32, 1)
