'''
 Escreva um programa que leia um número N inteiro qualquer e
 mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
'''

print('-' * 20)
print('SEQUENCIA DE FIBONACCI')
print('-' * 20)

cont = int(input('Quantos termos você quer mostrar: '))
fib = 0
num = pos = 1
print(f'{fib} => ', end='')
while num < cont:
    fib, pos = pos, fib + pos
    print(f'{fib} => ', end='')
    num += 1
print('FIM')