
jogador = {}
gols = []
jogadores = []

while True:
    jogador['nome'] = input('Nome do Jogador: ')
    jg = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))

    for j in range(1, jg+1):
        gols.append(int(input(f'Quantos gols na partida {j}? ')))

    jogador['gols'] = gols.copy()
    gols.clear()
    jogadores.append(jogador.copy())
    jogador.clear()

    while True:
        opc = input('Quer continuar? [S/N] ').lower()
        if opc not in 'ns':
            print('ERRO! Digite novamente!')
            continue
        else:
            break
    if opc == 'n':
        break
    else:
        continue

print('-=' * 50)
print(f'{"cod":<3}{"nome":>5}{"gols":>25}{"total":>30}')
print('-'*65)

for i, d in enumerate(jogadores):
    print(f'{i:>3} {d["nome"]:<25}{str(d["gols"]):<29}{sum(d["gols"]):<5}')
print('-'*65)

while True:
    op = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if op == 999:
        break

    for i, d in enumerate(jogadores):
        if op == i:
            print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[i]["nome"]}')
            for a, b in enumerate(jogadores[i]['gols']):
                print(f'No jogo {a} fez {b} gols.')
    print('-' * 65)


