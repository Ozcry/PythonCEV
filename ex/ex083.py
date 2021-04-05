'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses abertos e fechados na ordem correta.'''
exp = str(input('Digite a expressão: ')).strip().upper()
conta = contf = sim = soma = 0
contafl = []
for c in exp:
    if c == '(':
        conta += 1
        contafl.append(1)
    if c == ')':
        contf -= 1
        contafl.append(-1)
if conta + contf == 0:
    sim += 1
for v in contafl:
    soma += v
    if soma == 0:
        sim += 1
if contafl[0] == 1:
    sim += 1
if contafl[-1] == -1:
    sim += 1

if sim == 4:
    print('Sua expressão esta valida!!')
else:
    print('Sua expressão esta errada!!')
