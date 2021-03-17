### Crie um programa que leia um frase pelo teclado e mostre:
### > Quantas vezes aparece a letra "A".
### > Em que posição ela aparece a primeira vez.
### > Em que posição ela aparece a última vez.
texto = str(input('digite alguma coisa: ')).strip().upper()
print(texto.count('A'))
print(texto.find('A') + 1)
print(texto.rfind('A') + 1)
