'''
tuplas = ()
listas = []
dicionários = {}
dicionários = dict()
'''

'''
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados['sexo'])
del dados['idade']
'''

'''
filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')
'''

'''e possivel colocar dicionario dentro de listas e tuplas'''

###Brincando

'''
pessoas = {'nome': 'Jean', 'sexo': 'M', 'idade': 23}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# del pessoas['sexo']
pessoas['nome'] = 'Mol'
pessoas['peso'] = 65
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''

'''
brasil = []
estado = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
brasil.append(estado)
brasil.append(estado2)
print(estado)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
'''

'''
estado = dict()
brasil = list()
for c in  range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
for e in brasil:
    for v in e.values():
        print(v)
'''
