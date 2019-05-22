lista = []
cont = 0

while True:
    x = int(input('Digite um valor: '))
    lista.append(x)
    valid_opc = False
    while valid_opc == False:
        opc = input('Deseja continuar [S/N] ?:  ').strip().lower()
        if opc[0] in 'sn':
            valid_opc = True
        else:
            print('Digite uma opção valida')
    if opc == 'n':
        break


print('=' * 15)
print(f'\nVocê digitou {len(lista)} elementos!')
print(f'Os valores em ordem decrescentes são {sorted(lista,reverse=True)}')

if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')