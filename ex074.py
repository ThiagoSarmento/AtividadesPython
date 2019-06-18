'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso,mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
'''

from random import randint

tupla = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))

print(f'Os valores sorteados foram: {tupla[0]} {tupla[1]} {tupla[2]} {tupla[3]} {tupla[4]}')

print(f'O maior valor é: {max(tupla)}')
print(f'O menor valor é: {min(tupla)}')