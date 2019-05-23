lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    opc = input('Deseja continuar [S/N]? ').lower().strip()
    if opc == 'n':
        break

par = []
impar = []
for x in lista:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de impares é : {impar}')
