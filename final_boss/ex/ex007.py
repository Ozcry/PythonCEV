'''-> Crie um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''
from final_boss.modulos import mat, texto
texto.linha(33, 1)
nome = texto.leianome('Nome do aluno? ', 34)
n1 = mat.leianumfi('Digite a primeira nota: ', 35)
n2 = mat.leianumfi('Digite a segunda nota: ', 37)
texto.linha(sty=1)
texto.escreva(f'A média do aluno {nome} foi {mat.media(n1, n2)}', 36)
texto.linha(33, 1)
texto.escreva('FIM', 32, 1)
