def resumo(num, ad):
    print('\033[1;33m-=\033[m' * 20)
    print(f'\033[1;36m{"RESUMO DO VALOR":^40}\033[m')
    print('\033[36m--\033[m' * 20)
    print(f'\033[33m{"Preço analisado:":<25}\033[m', end='')
    print(f'{moeda(num):<15}')
    print(f'\033[32m{"Dobro do preço:":<25}\033[m', end='')
    print(f'{dobro(num, True):<15}')
    print(f'\033[37m{"Metade do preço:":<25}\033[m', end='')
    print(f'{metade(num, True):<15}')
    pf = str(ad)
    if ad > 0:
        if len(pf) == 1:
            print(f'\033[31m{ad}{"% de aumento:":<24}\033[m', end='')
            print(f'{aumento(num, ad, True):<15}')
        if len(pf) == 2:
            print(f'\033[31m{ad}{"% de aumento:":<23}\033[m', end='')
            print(f'{aumento(num, ad, True):<15}')
        if len(pf) == 3:
            print(f'\033[31m{ad}{"% de aumento:":<22}\033[m', end='')
            print(f'{aumento(num, ad, True):<15}')
        if len(pf) >= 4:
            print(f'\033[31m{ad}{"% de aumento:":<21}\033[m', end='')
            print(f'{aumento(num, ad, True):<15}')
    else:
        if len(pf) == 2:
            print(f'\033[31m{ad * -1}{"% de redução:":<24}\033[m', end='')
            print(f'{aumento(num, ad, True):<15}')
        if len(pf) == 3:
            print(f'\033[31m{ad * -1}{"% de redução:":<23}\033[m', end='')
            print(f'{aumento(num, ad, True):<15}')
        if len(pf) == 4:
            print(f'\033[31m{ad * -1}{"% de redução:":<22}\033[m', end='')
            print(f'{aumento(num, ad, True):<15}')
        if len(pf) >= 5:
            print(f'\033[31m{ad * -1}{"% de redução:":<21}\033[m', end='')
            print(f'{aumento(num, ad, True):<15}')
    print('\033[1;33m-=\033[m' * 20)
    print('\033[1;32mFIM\033[m')


def aumento(num, aum=0, form=False):
    if form:
        return moeda(num + (num * aum / 100))
    else:
        return num + (num * aum / 100)


def dobro(num, form=False):
    if form:
        return moeda(num * 2)
    else:
        return num * 2


def metade(num, form=False):
    if form:
        return moeda(num / 2)
    else:
        return num / 2


def moeda(num):
    aux = f'R${float(num):.2f}'
    aux2 = str(aux)
    aux3 = aux2.replace('.', ',')
    return aux3


def leiainteiro(num):

    def teste(n1):
        aux2 = n1
        try:
            int(aux2)
        except ValueError:
            return False
        return aux2

    aux = input(num).strip()

    while not teste(aux):
        print(f'\033[31mERRO: "{aux}" é um valor inválido! Por favor, digite um número inteiro válido.\033[m')
        aux = input(num).strip()
    return aux


def leiafloat(num):

    def teste(n1):
        aux2 = n1.replace(',', '.')
        try:
            float(aux2)
        except ValueError:
            return False
        return True

    aux = input(num).strip()

    while not teste(aux):
        print(f'\033[31mERRO: "{aux}" é um valor inválido! Por favor, digite um número real válido.\033[m')
        aux = input(num).strip()
    if len(aux) == 1:
        aux2 = int(aux)
        return f'{aux2:.1f}'.replace(',', '.')
    else:
        return aux.replace(',', '.')
