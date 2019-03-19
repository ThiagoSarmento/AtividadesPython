'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from time import  sleep
from random import randint

lista = ('Pedra', 'Papel', 'Tesoura')

print('''
SUAS OPÇÕES:
[0] Pedra 
[1] Papel
[2] Tesolra
''')

jogada = int(input('Qual a sua jogada: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')

comp = randint(0, 2)

print('=' * 20)
print(f'Computador jogou {lista[comp]}')
print(f'Jogador jogou {lista[jogada]}')
print('=' * 20)


if comp == 0:
    if jogada == 0:
        print('EMPATE')
    elif jogada == 1:
        print('JOGADOR VENCE')
    elif jogada == 2:
        print('COMPUTADOR VENCE')
elif comp == 1:
    if jogada == 0:
        print('computador vence')
    elif jogada == 1:
        print('EMPATE')
    elif jogada == 2:
        print('JOGADOR VENCE')
elif comp == 2:
    if jogada == 0:
        print('JOGADOR VENCE')
    elif jogada == 1:
        print('COMPUTADOR VENCE')
    elif jogada == 2:
        print('EMPATE')