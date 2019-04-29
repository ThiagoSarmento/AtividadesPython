'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi
o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
'''

lista = []
ct = 0

while True:
    lista.append(int(input('Digite um valor: ')))
    ct += 1
    cont = input('Deseja continuar [S/N]: ')
    if cont in 'Nn':
        break
    elif cont in 'Ss':
        continue
    elif cont not in 'SsNn':
        print('Opção Inválida. Digite novamente')
        cont = input('Deseja continuar [S/N]: ')
        if cont in 'Nn':
            break
        elif cont in 'Ss':
            continue

media = sum(lista) / ct
print(f'Você digitou {ct} números e a média foi {media}')
print(f'O maior valor foi {max(lista)} e o menor valor foi {min(lista)}')