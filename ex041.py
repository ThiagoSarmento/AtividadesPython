'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
from datetime import date

nasc = int(input('Informe o ano de nascimento: '))
ano = date.today().year
idadade = ano - nasc

print(f'O atleta tem {idadade} anos')

if idadade <= 9:
    print('Classificação: MIRIM')
elif idadade <= 14:
    print('Classificação: INFANTIL')
elif idadade <= 19:
    print('Classificação: JÚNIOR')
elif idadade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
