'''
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número
solicitado for negativo.
'''

while True:

    num = int(input('Quer ver a tabuada de qual número: '))
    print('-' * 20)

    if num <= 0:
        break

    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    print('-' * 20)

print('Tabuada errada! Volte sempre!!')