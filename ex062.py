'''
 Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

print('Gerador de PA')
print('=' * 20)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

cont = 1
valida = True
while cont < 11:
    print(f'{primeiro} => ', end='')
    primeiro += razao
    cont += 1
print('PAUSA')

num = 10
while valida == True:
    cont = int(input('Quantos termos você quer mostrar a mais: '))
    num += cont
    if cont == 0:
        valida = False
    else:
        while cont > 0:
            print(f'{primeiro} => ', end='')
            primeiro += razao
            cont -= 1
        print('PAUSA')
print(f'Progressão finalizada com {num} mostrados!!')