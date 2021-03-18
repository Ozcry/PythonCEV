### Estrutura condicional -- simples quando não tem o ''else'' composta quando o tem
'''
if carro.esquerda():
    bloco true
else:
    bloco false
'''

### condição composta
'''
tempo = int(input('Quantos anos ntem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('---FIM---')
'''

### condição simplificada
'''
tempo = int(input('Quantos anos ntem seu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('---FIM---')
'''

###Brincando

### Condição composta
'''
nome = str(input('Qual e o seu nome? ')).strip().capitalize()
if nome == 'Jean':
    print('Que nome lindo vc tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
'''

### Condição composta
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Você foi aprovado, PARABÊNS!')
else:
    print('Você foi reprovado, estude mais da proxima vez!')
'''

### Condição simplificada
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
print('PARABÊNS!' if m >= 6 else 'Estude mais!')
'''
