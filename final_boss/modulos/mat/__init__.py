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
