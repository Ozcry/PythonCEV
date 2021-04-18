'''Reescreva a função leiaInt() que fizemos no DESAFIO 104, incluindo agora a possibilidade da digitação de um número de
tipo inválido. Aproveite e crie também uma função leiaFloot() com a mesma funcionalidade.'''
from utilidadesCeV import moeda, texto
n1 = moeda.leiainteiro('\033[34mDigite um Inteiro:\033[m ')
n2 = moeda.leiafloat('\033[35mDigite um Real:\033[m ')
texto.linha()
print(f'\033[36mO valor inteiro digitado foi {n1} e o valor real foi {n2}\033[m')
texto.fim()
