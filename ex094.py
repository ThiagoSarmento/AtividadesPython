'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

dados = {}
cadastro = []
mulheres = []
soma = media = 0

while True:
    dados['nome'] = input('Nome: ')
    while True:
        genero = input('SEXO: [M/F]').lower()
        if genero not in 'mf':
            print('ERRO! Por favor, digite apenas M ou F.')
            continue
        else:
            break
    dados['sexo'] = genero
    dados['idade'] = int(input('Idade: '))
    while True:
        opc = input('Deseja Continuar: [S/N] ').lower()
        if opc not in 'sn':
            print('ERRO! Responda somente S ou N.')
            continue
        else:
            break
    cadastro.append(dados.copy())

    if opc == 'n':
        break
    else:
        continue

print('-=' * 30)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')

for d in cadastro:
    for k, v in d.items():
        if k == 'idade':
            soma += d[k]
        elif v == 'f':
            mulheres.append(d['nome'])
media = soma / len(cadastro)

print(f'B) A média da idade é de {media:.2f} anos.')

print('C) As mulheres cadastradas foram ', end='')
for m in mulheres:
    print(f'{m} ', end='')
print()

print(f'D) Lista de pessoas que estão acima da média: ')
for d in cadastro:
    if d['idade'] > media:
        print(f'nome = {d["nome"]}; sexo = {d["sexo"]}; idade = {d["idade"]}.')
print('<< ENCERRADO >>')

