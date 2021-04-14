'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o
processo de cálculo do fatorial.'''


def fatorail(num, show=False):
    """==> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n."""
    print('\033[1;33m-=\033[m' * 20)
    f = 1
    if show:
        for c in range(num, 0, -1):
            f *= c
            print(f'\033[34m{c}\033[m ', end='')
            if c != 1:
                print(f'\033[35m{"x"}\033[m ', end='')
            else:
                print(f'\033[35m{"="} \033[m', end='')
                return f
    else:
        for c in range(num, 0, -1):
            f *= c
        return f


print(fatorail(5, True))
print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
