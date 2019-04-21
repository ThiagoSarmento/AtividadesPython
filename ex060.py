'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

n1 = int(input('Digite um número\n'
               'para calcular o seu fatorial: '))

n2 = 1

print(f'Calculando o {n1}! = ', end=' ')
while n1 >=1 :
    n2 *= n1
    print(f'{n1} X', end=' ')
    n1 -= 1

print(f'= {n2}')
