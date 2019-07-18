'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante
o campeonato.
'''

cadastro = {}
lista = []

cadastro['nome'] = input('Nome do jogador: ')

jg = int(input(f'Quantas partidas {cadastro["nome"]} jogou?'))
for j in range(1, (jg+1)):
    lista.append(int(input(f'Quantos gols na partida {j}: ')))


cadastro['gols'] = lista.copy()
cadastro['total'] = sum(lista)
print('-=' * 30)
print(cadastro)
print('-=' * 30)

for k, v in cadastro.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)

print(f'O jogador {cadastro["nome"]} jogou {len(cadastro["gols"])} partidas.')
for i, v in enumerate(cadastro['gols']):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {cadastro["total"]}')


