'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
a tabela abaixo
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''
peso = float(input('\033[33mDigite o seu peso em Kg:\033[m '))
altura = float(input('\033[33mDigite a sua altura em M:\033[m '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('\033[31mVocê esta abaixo do peso ideal.\033[m')
elif 18.5 <= imc < 24.9:
    print('\033[30mVocê esta com o peso ideal.\033[m')
elif 25 <= imc < 29.9:
    print('\033[32mVocê esta com sobrepeso.\033[m')
elif 30 <= imc < 40:
    print('\033[34mVocê esta obeso.\033[m')
else:
    print('\033[35mVocê esta com Obesidade mórbida.\033[m')
