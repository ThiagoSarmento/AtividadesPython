'''
Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até dez. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')


while True:
    try:
        x = int(input('Digite um número entre 0 e 10 (-1 para sair): '))
        if x > 10:
            print('Tente Novamente!!!')
        elif x >= 0 and x <= 10:
            print(f'Você digitou o número {num[x]}')
        else:
            break
    except:
        print('Valor inválido. Encerrando')
        break