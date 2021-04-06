'''
dados = ['pedro', 25]
pessoas = []
pessoas.append(dados[:])
print(len(pessoas))
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
'''

### Brincando
'''
teste = list()
teste.append('Jean')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''

'''
galera = [['João', 19], ['Ana', 33], ['Joaquin', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''

'''
galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado. append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0].capitalize()} é maior de idade.')
    else:
        print(f'{p[0].capitalize()} é menor de idade.')
'''
