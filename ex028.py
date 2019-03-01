"""Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)
n0 = int(input('Em que número eu pensei: '))
n1 = randint(0, 6)
print('processando...')
sleep(1)

if n0 == n1:
    print('Parabens! Você venceu!')
else:
    print(f'Ganhei!! Você escolheu {n0} e eu pensei em {n1}!!')
