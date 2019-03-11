'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou
do prazo.
'''

from datetime import date

ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano

print(f'Quem nasceu em {ano} tem {idade} em {atual}')

if idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} ano(s)\n'
          f'Seu alistamento foi em {atual - (idade - 18)}')
elif idade == 18:
    print(f'Você deve se alistar em IMEDIATAMENTE!')
elif idade < 18:
    print(f'Seu alistamento será daqui ha {18-idade} anos, \n'
          f'seu alistamento será no ano de {(18 -idade) + atual}')
