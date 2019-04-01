'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
'''

frase = str(input('Digite uma frase: ')).strip()
frase = frase.split()
frase = ''.join(frase)
inverso = ''
for i in range(len(frase)-1, -1, -1):
    inverso += frase[i]


print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('Temos um palíndromo')
else:
    print('Não temos um palindromo!')