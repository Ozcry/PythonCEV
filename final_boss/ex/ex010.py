'''-> Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar,
obs(US$1,00 = R$3,27)'''
from final_boss.modulos import texto, mat
texto.linha(33, 1, 30)
n1 = mat.leianumfi('Quantos de dinheiro você tem? ', 34)
n2 = mat.leianumfi('Quanto esta valendo o dólar? ', 35)
texto.linha(sty=1)
texto.escreva(f'{mat.dinheiro(n1)} valem {mat.dinheiro(mat.real_dolar(n1, n2))}', 36)
texto.linha(33, 1, 30)
texto.escreva('FIM', 32, 1)
