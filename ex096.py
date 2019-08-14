'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de
um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def area():
    print(f'{"CONTROLE DE TERRENOS":^30}')
    print('-' * 30)
    b = float(input('Largura (m): '))
    a = float(input('Comprimento (m): '))
    area = b * a
    print(f'A área de um terreno de {b} X {a} é de {area}m²')



area()

