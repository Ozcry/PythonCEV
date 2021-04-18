'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
from utilidadesCeV import texto
import requests
texto.linha()
try:
    site = requests.get('https://www.youtube.com/watch?v=8jAykqxIeqw&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=50')
except:
    print('\033[35mNo momento o site está fora do ar!\033[m')
else:
    print('\033[34mO site está online!!\033[m')
texto.fim()
