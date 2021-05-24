'''-> Crie um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.'''
from final_boss.modulos import mat, texto
texto.linha(33, 1, 30)
num = mat.leiaint('Digite um número inteiro para ver a tabuada: ', 34)
ate = mat.leiaint('Deseja ver a tabuada ate que quantos? ', 36)
texto.linha(sty=1)
texto.escreva(f'{f"TABUADA DO {num}":^40}', 31)
texto.linha(sty=1)
mat.tabuada(num, ate, 35)
texto.linha(33, 1, 30)
texto.escreva('FIM', 32, 1)
