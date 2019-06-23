'''
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

lista = ('lapis', 2.50,
         'caderno', 16.0,
         'caneta', 3.0,
         'apontador', 4.5,
         'borracha', 1.5,
         'lapiseira', 8.0)

print('=' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('=' * 40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:<30}', end=' ')
    else:
        print(f'{lista[pos]:>7.2f}')
print('=' * 40)
