'''
Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade = float(input('Qual é a velocidade atual do carro: '))
limite = 80.00
acima = velocidade - limite
multa = acima * 7

if velocidade <= limite:
    print(f'Tenha um bom dia. Dirija com cuidado!!!')
else:
    print(f'MULTADO!! Você excedeu o limite que é de 80km/h.'
          f'\nVocê deve pagar uma multa de R${multa:.2f}')
