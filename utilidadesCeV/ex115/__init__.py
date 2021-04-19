def menu():
    from time import sleep
    sair = 0
    while sair != 3:
        print('\033[1;33m-=\033[m' * 30)
        print(f'{"MENU PRINCIPAL":^60}')
        print('\033[1;33m-=\033[m' * 30)
        print('\033[33m1\033[m -\033[34m Ver pessoas cadastradas\033[m')
        print('\033[33m2\033[m -\033[34m Cadastrar nova Pessoa\033[m')
        print('\033[33m3\033[m -\033[34m Sair do Sistema\033[m')
        print('\033[1;33m-=\033[m' * 30)
        op = opcao('\033[32mSua Opção:\033[m ')
        print('\033[1;33m-=\033[m' * 30)
        if op == 1:
            print(f'{"PESSOAS CADASTRADAS":^60}')
            print('\033[1;33m-=\033[m' * 30)
            try:
                arquivo = open('cadastro.txt', 'r')
            except:
                arquivo = open('cadastro.txt', 'w')
                arquivo.close()
            else:
                print(arquivo.read().rstrip())
                arquivo.close()
        elif op == 2:
            print(f'{"NOVO CADASTRO":^60}')
            print('\033[1;33m-=\033[m' * 30)
            nome = opcao3('Nome: ')
            try:
                arquivo = open("cadastro.txt", "a")
            except:
                arquivo = open('cadastro.txt', 'w')
                arquivo.close()
            else:
                arquivo.write(f'{nome:<45}{opcao2("Idade: "):<3}anos\n')
                arquivo.close()
            finally:
                print(f'Novo registro de {nome} adicionado.')
        elif op == 3:
            sair += 3
    print(f'\033[1;32m{"Saindo do sistema... Até logo!"}\033[m')


def opcao(valor):
    lista = ['1', '2', '3']
    b = input(valor).strip()
    while b not in lista:
        try:
            int(b)
        except ValueError:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            b = input(valor).strip()
        else:
            print('\033[31mERRO: digite uma opção válida.\033[m')
            b = input(valor).strip()
    return int(b)


def opcao2(valor):
    b = input(valor).strip()
    sair = 0
    while sair == 0:
        try:
            int(b)
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            b = input(valor).strip()
        else:
            sair += 1
    return b


def opcao3(valor):
    b = input(valor).strip().title()
    a = b.replace(' ', '')
    sair = 0
    while sair == 0:
        if a.isalpha():
            sair += 1
        else:
            print('\033[31mERRO: por favor, digite um nome válido.\033[m')
            b = input(valor).strip().title()
            a = b.replace(' ', '')
    return b
