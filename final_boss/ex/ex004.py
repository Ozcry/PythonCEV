'''-> Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiceis
sobre ele.'''
from final_boss.modulos import utilidades, texto

texto.linha(33)
aux = texto.leiatudo('Digite qualquer coisa: ', 31)
texto.linha(33)
utilidades.informacoes(aux)
texto.linha(33)
texto.escreva('FIM', 32, 1)
