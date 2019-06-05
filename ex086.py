# lista = [[], [], []]
# maior = somac = soma = 0
#
# for x in range(0,3):
#     for y in range(0,3):
#         a = int(input(f'Digite o valor para a posição [{x}, {y}]: '))
#         lista[x].append(a)
#
# print('-=' * 20)
# for val in lista:
#     print(val)
#
# for num in lista:
#     for i in num:
#         if i % 2 == 0:
#             soma += i
# print(f'\nA soma de todos os valores pares da matriz é: {soma}')
#
# for num2 in lista:
#     somac += num2[2]
#
# print(f'A soma dos valores da terceira coluna é: {somac} !!')
#
# maior = max(lista[1])
#
# print(f'O maior valor da segunda coluna é {maior}')

lista = [[], [], []]
validNum = False
maior = somaPar = somaTer = 0
lista2 = []

for a in range(0, 3):
    for b in range(0, 3):
        num = input(f'Digite um número inteiro para a posição [{a}:{b}]: ')
        while validNum == False:
            try:
                num = int(num)
                lista[a].append(num)
                validNum = True
            except:
                print('Digite somente números inteiros!!!')
                continue
        validNum = False

print('-=' * 20)
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{lista[x][y]:^5}]',end='')
    print()

print('-=' * 20)
for d in lista:
    for e in d:
        if e % 2 == 0:
            somaPar += e
print(f'A soma de todos os valores pares é: {somaPar}')

for f in lista:
    somaTer += f[2]
print(f'A soma dos valores da terceira coluna é: {somaTer}')

for g in lista:
    lista2.append(g[1])
    maior = max(lista2)
print(f'O maior valor da segunda coluna é: {maior}')
