'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo
'''
from random import randint
cont = 0
comp = randint(1, 5)
opc = ' '
soma = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)

while True:
    num = int(input('Diga um valor de 0 a 5: '))
    opc = input('Par ou Impar [P/I]: ').lower()
    soma = comp + num

    print('-' * 40)
    print(f'Você jogou {num} e o computador jogou {comp}.',end=' ')

    if soma % 2 == 0 and opc == 'p':
        print(f'Total de {soma}. Deu PAR.')
        print('-' * 40)
        print('Você venceu!')
        print('Vamos jogar novamente...')
    elif soma % 2 == 0 and opc == 'i':
        print(f'Total de {soma}. Deu PAR.')
        print('-' * 40)
        print('Você perdeu!')
        break
    elif soma % 2 !=0 and opc == 'i':
        print(f'Total de {soma}. Deu IMPAR.')
        print('-' * 40)
        print('Você venceu!')
        print('Vamos jogar novamente...')
    elif soma % 2 !=0 and opc == 'p':
        print(f'Total de {soma}. Deu IMPAR.')
        print('-' * 40)
        print('Você perdeu!')
        break

    cont += 1

print('=-' * 20)
print(f'GAMER OVER. Você venceu {cont} vezes.')