'''-> Crie um programa que leia um numero e mostre o seu dobro, triplo e raiz quadrada.'''
from final_boss.modulos import mat, texto

texto.linha(33, 1)
n1 = mat.leiaint('Digite um número: ', 35)
texto.escreva(f'Você digitou {n1}, o dobro e {mat.dobro(n1)}, o triplo e {mat.triplo(n1)} é a raiz quadrade vale {mat.raizqua(n1):.2f}', 36)
texto.linha(33, 1)
texto.escreva('FIM', 32, 1)
