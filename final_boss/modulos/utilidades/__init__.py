def informacoes(valor):
    """
    Função que passar algumas informações sobre um objeto.
    :param valor: Objeto que deseja receber informações
    :return: Nada
    """
    from final_boss.modulos import texto
    texto.escreva(f'Está em maiúsculo? {valor.isupper()}', 36)
    texto.escreva(f'Está em minusculo? {valor.islower()}', 36)
    texto.escreva(f'Todas as primeiras letra são maiúsculas? {valor.istitle()}', 36)
    texto.escreva(f'É um espaço em branco? {valor.isspace()}', 36)
    texto.escreva(f'É um número natural? {valor.isnumeric()}', 36)
    texto.escreva(f'É um possível nome de variável valido? {valor.isidentifier()}', 36)
    texto.escreva(f'Todos os caracteres são dígitos? {valor.isdigit()}', 36)
    texto.escreva(f'Pode ser representado como um caractere US-ASCII de 7 bits, válido? {valor.isascii()}', 36)
    texto.escreva(f'Todos os caracteres são letras? {valor.isalpha()}', 36)
