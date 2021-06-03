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
    return igual_int_float(soma)


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


def suce(num):
    """
    Função para calcular sucessor de um número.
    :param num: Número para se obter o sucessor
    :return: Sucessor
    """
    return num + 1


def ante(num):
    """
    Função para calcular antecessor de um número.
    :param num: Número para se obter o antecessor
    :return: Antecessor
    """
    return num - 1


def dobro(num):
    """
    Função para calcular o dobro de um número.
    :param num: Número para obter o dobro
    :return: Dobro de um número
    """
    return num * 2


def triplo(num):
    """
    Função para calcular o triplo de um número.
    :param num: Número para obter o triplo
    :return: Triplo de um número
    """
    return num * 3


def raizqua(num):
    """
    Função para calcular a raiz quadrada de um número.
    :param num: Número para obter a raiz quadrada
    :return: Raiz quadrada
    """
    return num ** (1/2)


def media(*num):
    '''
    Função para calcular a média de números.
    :param num: Números para calcular a média
    :return: Média dos números
    '''
    soma = 0
    for e in num:
        soma += e
    med = soma / len(num)
    return igual_int_float(med)


def igual_int_float(num):
    """
    Função para comparar se (número int) e igual a (número float).
    :param num: Número para se comparar
    :return: Número (int) ou (float)
    """
    if int(num) == float(num):
        return int(num)
    else:
        return float(num)


def metros_centimetros(valor):
    """
    Função para converter um valor em metros para centímetros.
    :param valor: Valor a ser convertido
    :return: Valor em centímetros
    """
    return valor / 0.01


def metros_milimetros(valor):
    """
    Função para converter um valor em metros para milímetros.
    :param valor: Valor a ser convertido
    :return: Valor em milímetros
    """
    return valor / 0.0010000


def tabuada(num, ate, cor=0, sty=0):
    """
    Função para mostrar a tabuada de um número.
    :param num: Número a ser multiplicado
    :param ate: Multiplicar ate atingir esse valor
    :param cor: Cor de exibição da tabuada (30 a 37)
    :param sty: Style de exibição da tabuada (0, 1, 4, 7)
    :return: Nada
    """
    from final_boss.modulos import texto
    for e in range(1, ate + 1):
        texto.escreva(f'{num} * {e} = {num * e}', cor, sty)


def dinheiro(num):
    """
    Função para retornar um valor em formato monetário.
    :param num: Número a ser convertido
    :return: Uma str no formato monetário
    """
    aux = f'{float(num):.2f}'
    aux2 = str(aux)
    aux3 = aux2.replace('.', ',')
    return f'R$ {aux3}'


def real_dolar(real, dolar):
    """
    Função para converter real em dólar.
    :param real: Valor em real
    :param dolar: Cotação atual do dólar
    :return: Retorna o valor em real convertido para dólar
    """
    return real / dolar
