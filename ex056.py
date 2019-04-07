'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

somaidade = 0
cont = 0

for i in range(1, 5):
    print(f'-----{i}ª Pessoa-----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').lower()

    somaidade += idade

    if i == 1 and sexo == 'm':
        nomeV = nome
        idaV = idade
    elif idaV < idade and sexo =='m':
        nomeV = nome
        idaV = idade

    if sexo == 'f' and idade < 20:
        cont += 1


media = somaidade / 4

print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {idaV} anos e se chama {nomeV}')
print(f'Ao todo são {cont} mulheres com menos de 20 anos')
