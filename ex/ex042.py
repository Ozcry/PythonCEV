'''Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: Todos os lados iguais
- Isósceles: Dois lados iguais
- Escaleno: Todos os lados diferentes'''
print('\033[33;47m=-=\033[m' * 20)
r1 = float(input('\033[34mDigite o tamanho da primeira reta:\033[m '))
r2 = float(input('\033[35mDigite o tamanho da segunda reta:\033[m '))
r3 = float(input('\033[36mDigite o tamanho da terceira reta:\033[m '))
if r1 < r2 + r3 and r1 > r2 - r3 and r2 < r1 + r3 and r2 > r1 - r3 and r3 < r1 + r2 and r3 > r1 - r2:
    if r1 == r2 == r3:
        print('\033[32mPode formar um triângulo é ele sera Equilátero.\033[m')
    elif r1 != r2 != r3:
        print('\033[33mPode formar um triângulo é ele sera Escaleno.\033[m')
    else:
        print('\033[37mPode formar um triângulo é ele sera Isóceles.\033[m')
else:
    print('\033[31mNão pode ser um triângulo!\033[m')
print('\033[33;47m=-=\033[m' * 20)
