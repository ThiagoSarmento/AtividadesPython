'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos
os valores únicos digitados, em ordem crescente.
'''


lista = []

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!!')
    else:
        print('Valor duplicado! Não vou adicionar!!')
    op = input('Deseja Continuar ? [N/S]')
    if op.lower() == 'n':
        break
    else:
        continue
lista.sort()
print('-=' * 40)
print(f'Você digitou os valores {lista}')

