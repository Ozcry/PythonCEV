def menu():
    sair = 0
    while sair != 3:
        print('\033[1;33m-=\033[m' * 20)
        print(f'{"MENU PRINCIPAL":^40}')
        print('\033[1;33m-=\033[m' * 20)
        print('\033[33m1\033[m -\033[34m Ver pessoas cadastradas\033[m')
        print('\033[33m2\033[m -\033[34m Cadastrar nova Pessoa\033[m')
        print('\033[33m3\033[m -\033[34m Sair do Sistema\033[m')
        print('\033[1;33m-=\033[m' * 20)
        op = opcao('Sua Opção: ')
        print('\033[1;33m-=\033[m' * 20)
        if op == 1:
            print(f'{"PESSOAS CADASTRADAS":^40}')
            print('\033[1;33m-=\033[m' * 20)

        elif op == 2:
            print(f'{"NOVO CADASTRO":^40}')
            print('\033[1;33m-=\033[m' * 20)

        elif op == 3:
            sair += 3
    print(f'\033[1;32m{"Saindo do sistema... Até logo!"}\033[m')



'''
def opcao(num):

    def teste(n1):
        aux = n1
        try:
            int(aux)
        except ValueError:
            return False
        return True

    aux1 = ('1', '2', '3')
    aux2 = input('\033[36mSua Opção:\033[m ').strip()
    while aux2 not in aux1:
        while not teste(aux2):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            aux2 = input('\033[36mSua Opção:\033[m ').strip()
        print('\033[31mERRO: Digite uma opção válida!\033[m')
        aux2 = input('\033[36mSua Opção:\033[m ').strip()
    return int(aux2)
'''
