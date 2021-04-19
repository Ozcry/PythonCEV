### Tratamentos de erros e Exceções
'''
print(x) -> (exceção) erro semantico
primt(x) -> erro sintatico
'''

'''
try:
    operação
except:
    falou
else:
    deu certo
finally:
    certo/falha
'''

# Bricando

'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não e possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')
'''

# Correção ex113

'''
continue -> joga diretamente para o while novamente
'''
