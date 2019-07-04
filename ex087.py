'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

listas = [[], [], []]
somaT = soma = maioS = 0

for x in range(0, 3):
    for y in range(0, 3):
        listas[x].append(int(input(f'Digite um valor para [{x}:{y}]: ')))

print('-=' * 30)

for lista in listas:
    for i, v in enumerate(lista):
        print(f'[{v}]', end=' ')
        if v % 2 == 0:
            soma += v
        if i == 2:
            somaT += v
    print()

for i, v in enumerate(listas):
    if i == 1:
        for x in v:
            if x > maioS:
                maioS = x

print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {somaT}')
print(f'O maior valor da segunda linha é {maioS}')