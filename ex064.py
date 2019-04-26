'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
'''

valida = True
cont = soma = 0

while valida == True:
    num = int(input('Digite um número: [999 para sair]'))
    if num == 999:
        valida = False
    else:
        soma += num
        cont += 1

print(f'Você digitou {cont} e a soma entre eles foi {soma}')
