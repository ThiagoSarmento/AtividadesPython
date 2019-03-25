'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

s = 0
for i in range(1, 7):
    num = int(input(f'Digite o número {i}: '))
    if num % 2 == 0:
        s += num
print(f'A soma dos números pares é igual a {s}')

