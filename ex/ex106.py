'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS: use cores. '''


def escreva(texto):
    tam = len(texto) + 4
    print('\033[36m^\033[m' * tam)
    print(f'\033[37m  {texto}\033[m')
    print('\033[36m^\033[m' * tam)


print(f'\033[35m{"         SISTEMA DE AJUDA PyHELP"}\033[m')
print('\033[1;33m-=\033[m' * 20)


def sistema(a=input('\033[34mFunção ou Biblioteca >\033[m ')):
    from time import sleep
    while a != 'fim':
        escreva(f"Acessando o manual do comando '{a}'")
        sleep(0.5)
        help(a)
        print('\033[1;33m-=\033[m' * 20)
        sleep(0.5)
        a = input('\033[34mFunção ou Biblioteca >\033[m ')
    sleep(0.5)
    print('\033[1;33m-=\033[m' * 20)
    print('\033[1;32mFIM\033[m')


sistema()
