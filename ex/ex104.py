'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante á função input() do Python, só
que fazendo a validação para aceitar apenas um valor numérico. Ex:. n = leiaInt('Digite um n: ')'''


def leiaint(valor):
    print('\033[1;33m-=\033[m' * 20)
    aux = input(valor)
    if aux.isdigit():
        return aux
    else:
        while not aux.isdigit():
            print('\033[1;31mERRO! Digite um número inteiro valido\033[m')
            aux = input(valor)
        return aux


n = leiaint('\033[35mDigite um número: \033[m')
print(f'\033[36mVocê acabou de digitar o número {n}\033[m')
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
