'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

s1 = int(input('Digite o primeiro segmento: '))
s2 = int(input('Digite o segundo segmento: '))
s3 = int(input('Digite o terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os seguimentos informados PODEM FORMAR um triângulo ', end='')
    if s1 != s2 != s3 != s1:
        print('ESCALENO')
    elif s1 == s2 == s3:
        print('EQUILÁTERO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos não podem formar um triângulo')


