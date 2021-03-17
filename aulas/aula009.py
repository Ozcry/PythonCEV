frase = 'Curso em Vídeo Python'
frase2 = '   Aprenda Python  '

'''pegar uma letra da string'''
print(frase[9])

'''pegar um pedaço da string'''
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

'''analisar strings'''
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

'''transformação em strings'''
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

'''Divisão de strings'''
print(frase.split())
print('-'.join(frase))

'''Escrever textos grandes na tela'''
print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""")

'''Brincando'''
print(frase.upper().count('O'))
print(len(frase2.strip()))
