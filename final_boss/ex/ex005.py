'''-> Crie um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.'''
from final_boss.modulos import mat, texto

texto.linha(33, 1)
num = mat.leianumfi('Digite um número: ', 36)
texto.escreva(f'Você digitou o número {num}, seu antecessor é {mat.ante(num)} e sucessor é {mat.suce(num)}', 34)
texto.linha(33, 1)
texto.escreva('FIM', 32, 1)
