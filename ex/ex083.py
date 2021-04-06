'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses abertos e fechados na ordem correta.'''
print('\033[1;33m-=\033[m' * 20)
exp = str(input('\033[34mDigite a expressão:\033[m ')).strip().upper()
conta = sim = 0
contafl = []
for c in exp:
    if c == '(':
        conta += 1
        contafl.append(1)
    if c == ')':
        conta -= 1
        contafl.append(-1)
if conta == 0:
    sim += 1
if contafl[0] == 1:
    sim += 1
if contafl[-1] == -1:
    sim += 1
if sim == 3:
    print('\033[36mSua expressão esta valida!!\033[m')
    print('\033[1;33m-=\033[m' * 20)
else:
    print('\033[35mSua expressão esta errada!!\033[m')
    print('\033[1;33m-=\033[m' * 20)
print('\033[1;32mFIM\033[m')
