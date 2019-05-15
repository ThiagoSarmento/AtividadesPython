'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre: A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.
'''


sM = sF = idM = 0

while True:
    opc = sexo = ' '
    print('-' *40)
    print('CADASTRE UMA PESSOA')
    print('-' * 40)

    idade = int(input('Idade: '))
    while sexo not in 'mf':
        sexo = input('Sexo[M/F]:  ').lower().strip()[0]
    print('-' * 40)

    if idade > 18:
        idM += 1
    if sexo == 'm':
        sM += 1
    if sexo == 'f' and idade < 20:
        sF += 1
    while opc not in 'sn':
        opc = input('Quer continuar [s/n]: ').lower().strip()[0]
    if opc == 'n':
        break
    else:
        continue

print(f'Total de pessoas com mais de 18 anos: {idM}')
print(f'Ao todo temos {sM} Homens cadastrados')
print(f'E temos {sF} mulheres com menos de 20 anos')