'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

lista = []
lista.append(int(input('Digite o primeiro valor: ')))
lista.append(int(input('Digite o segundo valor: ')))
print('')

valida = False

while valida == False:
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos Números\n'
          '[5] Sair do programa')
    opc = int(input('Qual é a sua opção: '))
    if opc == 1:
        print(f'A soma entre {lista[0]} + {lista[1]} é {lista[0] + lista[1]}')
    elif opc == 2:
        print(f'A multiplicação entre {lista[0]} X {lista[1]} é {lista[0] * lista[1]}')
    elif opc == 3:
        print(f'O maior valor entre {lista[0]} e {lista[1]} é {max(lista)}')
    elif opc == 4:
        lista[0] = int(input('Digite o primeiro valor: '))
        lista[1] = int(input('Digite o segundo valor: '))
    elif opc == 5:
        print('Saindo do programa!')
        valida = True
    else:
        print('Opção inválida! digite novamente!')
    print('======================')
