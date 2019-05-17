'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

print('=' * 40)
print(f'{"BANCO CEV":=^40}')
print('=' * 40)

valor = float(input('Qual valor deseja sacar: '))

saque = valor
ced = 50
totCed = 0

while True:
    if saque >= ced:
        saque -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} de R$ {ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if saque == 0:
            break

print('=' * 30)
print(f'Volte sempre ao banco CEV. ENCERRANDO.....')
