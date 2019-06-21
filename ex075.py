'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''


tupla = (int(input('Dite o valor 01: ')), int(input('Digite o valor 02: ')), int(input('Digite o valor 03: ')),
        int(input('Digite o valor 04: ')))

print('Você digitou os valores: ', end=' ')
for x in tupla:
    print(f'{x}', end=' ')

print(f'O valor 9 apareceu {tupla.count(9)}')
print(f'O valor 3 aparecer na {tupla.index(3)}º posição')

print('Os valores pares digitados foram: ', end= ' ')
for x in tupla:
    if x % 2 == 0:
        print(f'{x}', end=' ')

