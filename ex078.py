'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
maior = 0
menor = 0

lista = []
for x in range(1, 6):
    lista.append(int(input(f'Digite um valor para a posição {x}: ')))
    if x == 1:
        maior = menor = lista[0]
print('-=' * 30)
print(f'Você digitou os valores {lista}')

for num in range(0, len(lista)):

    if lista[num] >= maior:
        maior = lista[num]

    if lista[num] <= menor:
        menor = lista[num]


print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
        if v == maior:
            print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()

