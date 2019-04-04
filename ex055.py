'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

pesos = []

for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    pesos.append(peso)

print(f'O maior peso lido foi {max(pesos)}Kg.')
print(f'O menor peso lido foi {min(pesos)}Kg.')

