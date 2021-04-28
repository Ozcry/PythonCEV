def linha(cor=0, sty=0, tam=20):
    """
    Função para imprimir uma linha.
    :param cor: Cor da linha (30 a 37)
    :param tam: Tamanho da linha
    :param sty: Style da linha (0, 1, 4, 7)
    :return: Nada
    """
    print(f'\033[{sty};{cor}m-=\033[m' * tam)


def escreva(texto=' ', cor=0, sty=0):
    """
    Função para imprimir um texto.
    :param texto: Texto a ser imprimido
    :param cor: Cor da linha (30 a 37)
    :param sty: Style da linha (0, 1, 4, 7)
    :return: Nada
    """
    print(f'\033[{sty};{cor}m{texto}\033[m')


def leianome(texto=' ', cor=0, sty=0):
    """
    Função que funciona como um input para ler um nome.
    :param texto: Texto a ser exibido para o usuário
    :param cor: Cor da linha (30 a 37)
    :param sty: Style da linha (0, 1, 4, 7)
    :return: Retorna uma string (nome)
    """
    aux = input(f'\033[{sty};{cor}m{texto}').strip().title()
    aux2 = aux.replace(' ', '')
    sair = 0
    while sair == 0:
        if aux2.isalpha():
            sair += 1
        else:
            print('\033[31mERRO: por favor, digite um nome válido.\033[m')
            aux = input(f'\033[{sty};{cor}m{texto}').strip().title()
            aux2 = aux.replace(' ', '')
    return aux


def leiatudo(texto=' ', cor=0, sty=0):
    """
    Função que funciona como um input para ler tudo.
    :param texto: Texto a ser exibido para o usuário
    :param cor: Cor da linha (30 a 37)
    :param sty: Style da linha (0, 1, 4, 7)
    :return: Retorna uma string digitada pelo usuário
    """
    aux = input(f'\033[{sty};{cor}m{texto}')
    return aux
