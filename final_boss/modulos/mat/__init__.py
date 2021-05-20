def leianumfi(texto=' ', cor=0, sty=0):
    """
    Função que funciona como um input para ler um número funciona com int e float.
    :param texto: Texto a ser exibido para o usuário
    :param cor: Cor da linha (30 a 37)
    :param sty: Style da linha (0, 1, 4, 7)
    :return: Retorna um número
    """
    aux = input(f'\033[{sty};{cor}m{texto}\033[m').strip()
    aux2 = aux.replace(',', '.')
    sair = aux3 = 0
    while sair == 0:
        try:
            float(aux2)
        except:
            print('\033[31mERRO: por favor, digite um número válido.\033[m')
            aux = input(f'\033[{sty};{cor}m{texto}\033[m').strip()
            aux2 = aux.replace(',', '.')
        else:
            sair += 1
    try:
        aux3 = int(aux2)
    except:
        aux3 = float(aux2)
    finally:
        return aux3


def somanum(*num):
    """
    Função para somar números.
    :param num: Números que seram somados
    :return: Retorna a soma
    """
    soma = 0
    for e in num:
        soma += e
    if int(soma) == float(soma):
        return int(soma)
    else:
        return float(soma)


def leiaint(texto=' ', cor=0, sty=0):
    """
    Função que funciona como um input para ler um número inteiro.
    :param texto: Texto a ser exibido para o usuário
    :param cor: Cor do texto a ser exibido ao usuário (30 a 37)
    :param sty: Style do texto a ser exibido ao usuário (0, 1, 4, 7)
    :return: Retorna um número
    """
    aux = input(f'\033[{sty};{cor}m{texto}\033[m').strip()
    sair = 0
    while sair == 0:
        try:
            int(aux)
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            aux = input(f'\033[{sty};{cor}m{texto}\033[m').strip()
        else:
            sair += 1
    return int(aux)


def ansu(texto=' ', cori=0, styi=0, cor=0, sty=0):
    """
    Função que faz um print na tela do antecessor é sucessor de um número.
    :param texto: Texto a ser exibido para o usuário
    :param cori: Cor do texto a ser exibido ao usuário (30 a 37)
    :param styi: Style do texto a ser exibido ao usuário (0, 1, 4, 7)
    :param cor: Cor da resposta a ser exibido ao usuário (30 a 37)
    :param sty: Style da resposta a ser exibido ao usuário (0, 1, 4, 7)
    :return: Nada
    """
    aux = leiaint(texto, cori, styi)
    print(f'\033[{sty};{cor}mO número digitado foi {aux}, seu sucessor é {aux + 1} e seu antecessor é {aux - 1}\033[m')


def dobro(num):
    return num * 2


def triplo(num):
    return num * 3


def raizqua(num):
    return num ** (1/2)
