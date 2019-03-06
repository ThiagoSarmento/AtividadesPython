'''
Desenvolva um programa que leia o comprimento de três retas
 e diga ao usuário se elas podem ou não formar um triângulo.
'''

print('-=' * 20)
print('ANALISADOR DE TRIÂNGULO')
print('-=' * 20)

r1 = float(input('Digite o tamanho do primeiro lado: '))
r2 = float(input('Digite o tamanho do segundo lado: '))
r3 = float(input('Digite o tamanho do terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo com os valores informados')
else:
    print('Não é possível formar triangulo!!!')