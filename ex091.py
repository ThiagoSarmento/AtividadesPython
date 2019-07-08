'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jg01': randint(1, 6), 'Jg02': randint(1,6), 'Jg03': randint(1, 6), 'Jg04': randint(1, 6)}
ordem = []
for k, v in jogo.items():
    print(f'{k} resultado: {v}')
    sleep(0.5)

ordem = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('==== RANKING DE RESULTADOS ====')

for i, v in enumerate(ordem):
    print(f'{i+1}° LUGAR: {v[0]} com {v[1]}')
    sleep(0.5)

print(ordem)



