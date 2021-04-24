'''-> Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.'''
from final_boss.modulos import texto
texto.linha(33)
nome = texto.leianome('Digite seu nome: ', 35)
texto.linha(33)
texto.escreva(f'É um prazer te conhecer, {nome}!', 36)
texto.linha(33)
texto.escreva('FIM', 32, 1)
