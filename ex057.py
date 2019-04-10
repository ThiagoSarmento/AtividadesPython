'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

valida = False

while valida == False:
    sexo = input('Informe seu sexo: [M/F]')
    if sexo in 'MmFf':
        print(f'Sexo {sexo.upper()} registrado com sucesso!!')
        valida = True
    else:
        print('Dados inválidos! Por favor, ', end=' ')