def leiadinheiro(num):
    from utilidadesCeV import moeda

    def teste(n1):
        xua = n1.replace(',', '').replace('.', '')
        try:
            float(xua)
        except ValueError:
            return False
        return True

    aux = input(num).strip()
    while not teste(aux):
        print(f'\033[31mERRO: "{aux}" é um preço inválido!\033[m')
        aux = input(num).strip()
    por = int(input('\033[34mQuantos porcentos deseja aumentar ou diminuir?\033[m '))
    aux2 = aux.replace(',', '.')
    aux3 = float(aux2)
    return moeda.resumo(aux3, por)
