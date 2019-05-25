# lista = []
#
# lista.append(input('Digite uma expressão: '))
#
# for x in lista:
#     a = x.count('(')
#     b = x.count(')')
#     if a == b:
#         print('Sua expressão é válida!')
#     else:
#         print('Sua expressão esta errada!!')
#
# print(lista)

exp = input('Digite uma expressão: ')
pilha = []

for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão esta correta!')
else:
    print('Sua expressão esta errada!!')