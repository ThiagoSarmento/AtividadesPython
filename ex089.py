lista = []
aluno = []
nota = []

resp = 's'

while resp == 's':
    nome = input('Digite o nome do aluno: ')
    aluno.append(nome)

    for i in range(1, 3):
        num = float(input(f'Digite a {i}ª nota: '))
        nota.append(num)

    aluno.append(nota.copy())
    nota.clear()

    lista.append(aluno.copy())
    aluno.clear()

    resp = input('Deseja continuar [s/n] ?: ').lower().strip()

print('-='*30)
print('{:<4} {:<10} {:>8}'.format('Nº', 'NOME', 'MÉDIA'))

for a in lista:
    media = (sum(a[1]))/2
    print(f'{lista.index(a):<4} {a[0]:<10} {media:>8}')

print('-' * 26)

while True:
    mostrar = int(input('Mostrar as notas de qual aluno [999 para interromper] ?'))
    if mostrar == 999:
        break
    else:
        print(f'As notas de {lista[mostrar][0]} são {lista[mostrar][1]}')
        print('-' * 26)

print('Finalizando...')
print('<<<VOLTE SEMPRES>>>')
