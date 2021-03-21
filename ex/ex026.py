### Crie um programa que leia um frase pelo teclado e mostre:
### > Quantas vezes aparece a letra "A".
### > Em que posição ela aparece a primeira vez.
### > Em que posição ela aparece a última vez.
texto = str(input('\033[1;32;46mdigite alguma coisa:\033[m ')).strip().upper()
print('\033[35m', texto.count('A'), '\033[m')
print('\033[34m', texto.find('A') + 1, '\033[m')
print('\033[31m', texto.rfind('A') + 1, '\033[m')
