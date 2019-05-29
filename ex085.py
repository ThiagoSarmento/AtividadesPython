# pares = []
# impares = []
# i = 1
#
# while i < 8:
#
#     x = input(f'Digite o {i}º valor: ')
#
#     try:
#         x = int(x)
#
#         if x % 2 == 0:
#             pares.append(x)
#         else:
#             impares.append(x)
#
#         i += 1
#
#     except:
#         print('Digite somente números inteiros!!!')
#         continue
#
# print('-=' * 20)
# print(f'Os valores pares digitados foram: {sorted(pares)}')
# print(f'Os valores impares digitados foram: {sorted(impares)}')



# def validNum(num):
#     if num.isdigit():
#         return True
#     else:
#         print('Valor inválido, digite somente números inteiros!!')
#
# pares = []
# impares = []
# x = 1
#
# # while x < 8 :
#
#     valor = input(f'Digite o {x}º valor: ')
#
#     if validNum(valor):
#         if int(valor) % 2 == 0:
#             pares.append(valor)
#         else:
#             impares.append(valor)
#
#     x += 1
#
# print('-=' * 20)
#
# print(f'Os valores pares digitados foram: {sorted(pares)}')
# print(f'Os valores impares digiados forma: {sorted(impares)}')


lista = [[], []]

x = 1

while x < 8:
    num = input(f'Digite o {x}º valor: ')

    try:
        num = int(num)
        if num % 2 == 0:
            lista[0].append(num)
        else:
            lista[1].append(num)
    except:
        print('Digite somente números inteiros!!')
        continue

    x += 1

print('-=' * 20)
print(f'Todos os números digitados: {lista}')
print(f'Os números pares digitados foram: {lista[0]}')
print(f'Os números impares digitados foram {lista[1]}')