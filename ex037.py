'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das opções para conversão: 
[1] Converter para binário
[2] Converter para octal
[3] converter para hexadecimal''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} convertido para binário é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para octal é igula a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else:
    print(f'Opção inválida! Programa encerrado!!')
