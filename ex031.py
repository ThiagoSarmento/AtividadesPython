'''
 Desenvolva um programa que pergunte a distância de uma viagem em Km.
 Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
 e R$0,45 para viagens mais longas.
'''

km = float(input('Qual a distância da sua viagem: '))

if km <= 200.00:
    valor = km * 0.50
else:
    valor = km * 0.45

print(f'Você esta prestes a começar uma viagem de {km}km \n'
      f'E o preço da sua passagem será de R${valor}')
