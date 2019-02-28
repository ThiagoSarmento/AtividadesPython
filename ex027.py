""" Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente."""


n1 = str(input('Digite o seu nome: '))
n2 = n1.split()
print(f'Prazer em conher você {n1}')
print(f'Seu primeiro nome é {n2[0]}')
print(f'Seu último nome é {n2[len(n2)-1]}')