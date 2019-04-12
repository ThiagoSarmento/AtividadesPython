'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
'''

from random import randint

comp = randint(0, 3)

print('Sou seu computador...\n'
      'Acabei de pensar em um número entre 0 e 3.\n'
      'Será que você consegue adivinhar qual foi ?')


valida = False
cont = 0
while valida == False:
    cont += 1
    palp = int(input('Qual é o seu palpite: '))
    if palp > comp:
        print('Menos... Tente mais uma vez.')
    elif palp < comp:
        print('Mais... Tente mais uma vez.')
    else:
        print(f'Acertou com {cont} tentativas! Parabens!!')
        valida = True
