# from random import randint
# from time import sleep
# print('-'*30)
# print('{:^30}'.format('JOGO DA MEGA SENA'))
# print(('-'*30))
#
# num = int(input('Quantos jogos deseja sortear: '))
#
# print(f'-=-=-=SORTEANDO {num} JOGOS=-=-=-\n')
#
# for i in range(1, num+1):
#     jogo = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]
#     print(f'JOGO {i}: {jogo}')
#     sleep(1)
#
# print(f'\n-=-=-=-= !BOA SORTE! =-=-=-=-')

from random import randint
from time import sleep
jogo = []
jogos = []

print('-' * 30)
print('{:^30}'.format('JOGO DA MEGA SENA'))
print('-' * 30)

num = int(input('Quantos jogos deseja sortear:'))

print(f'\n -=-=-=SORTEANDO {num} JOGOS=-=-=- \n')

for i in range(1, num +1):
    jogo = [randint(0, 60), randint(0, 60), randint(0, 60),
            randint(0, 60), randint(0, 60), randint(0, 60)]
    jogos.append(jogo)

for a, b in enumerate(jogos):
    print(f'Jogo {a}: {b}')
    sleep(1)

print('\n-=-=-=-=-= BOA SORTE =-=-=-=-=-')