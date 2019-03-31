'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

num = int(input('Digite um número inteiro: '))
x = 0
for cont in range(1, num +1):
    print(f'{cont}', end=' ')
    if num % cont == 0:
        x += 1
print()
print(f'O número {num} foi divisível {x} vezes!')
if x > 2:
    print('Por esta razão ele não é primo')
else:
    print('e por isto ele é primo!!!')
