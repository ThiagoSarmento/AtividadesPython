'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''


caro = barato = tot = cont = 0
nome = ' '
while True:
    print('-' * 40)
    print('LOJA SUPER BARATÃO')
    print('-' * 40)
    prod = input('Nome do produto: ')
    valor = float(input('Preço R$: '))

    cont +=1
    tot += valor
    if valor > 1000:
        caro += 1

    if cont == 1 or valor < barato:

        barato = valor
        nome = prod

    opc = ' '
    while opc not in 'sn':
        opc = input('Quer continuar [s/n]: ').lower().strip()[0]
    if opc == 'n':
        break
    else:
        continue

print(f'{"FIM DO PROGRAMA":-^40}')
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {caro} custando mais de R$1000,00')
print(f'O produto mais barato foi {nome} custando {barato:.2f}')

