'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input(f'Em que ano a {i}º pessoa nasceu: '))
    if date.today().year - ano >= 18:
        maior += 1
    else:
        menor += 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade\n'
      f'e também tivemos {menor} menores de idade')
