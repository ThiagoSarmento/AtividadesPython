'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais
'''

tupla = ('programador', 'jogo', 'videogame', 'cachorro', 'gato', 'casa', 'praia', 'carro')


for p in tupla:
    print(f'Na palavra {p.upper()} temos: ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(f'{l}', end='')
    print()


