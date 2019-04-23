'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

print('Gerador de PA')
print('=' * 20)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

cont = 1

while cont < 11:
    print(f'{primeiro} => ', end='')
    primeiro += razao
    cont += 1
print('FIM')
