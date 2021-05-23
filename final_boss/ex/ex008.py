'''-> Crie um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.'''
from final_boss.modulos import mat, texto
texto.linha(33, 1)
valor = mat.leianumfi('Digite um valor em metros: ', 35)
texto.escreva(f'Você digitou {valor}m que corresponde a {mat.metros_centimetros(valor)}cm é {mat.metros_milimetros(valor)}mm', 36)
texto.linha(33, 1)
texto.escreva('FIM', 32, 1)
