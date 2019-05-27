pessoa = []
listaP = []
maior = []
menor = []

opc = 's'

while opc == 's':
    nome = input('Digite o nome: ').strip()
    peso = int(input('Digite o peso: '))
    pessoa.append(nome)
    pessoa.append(peso)
    listaP.append(pessoa.copy())
    pessoa.clear()
    opc = input('Deseja continuar [s/n] ? ').strip().lower()

for p in listaP:
    if len(maior) == 0:
        maior.append(p)
    else:
        if p[1] > maior[0][1]:
            maior.clear()
            maior.append(p)
        else:
            if p[1] == maior[0][1]:
                maior.append(p)

    if len(menor) == 0:
        menor.append(p)
    else:
        if p[1] < menor[0][1]:
            menor.clear()
            menor.append(p)
        else:
            if p[1] == menor[0][1]:
                menor.append(p)

print('=' * 30)
print(f'Ao todo você cadastrou {len(listaP)} pessoas')

temp = []
for x in maior:
    temp.append(x[0])
print(f'O maior peso foi de {maior[0][1]}. Peso de {temp}')

temp1 = []
for y in menor:
    temp1.append(y[0])
print(f'O menor pes foi de {menor[0][1]}. Peso de {temp1}')