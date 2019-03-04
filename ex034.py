'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%.
 Para os inferiores ou iguais, o aumento é de 15%.
'''

sal = float(input('Digite o valor do salário: '))

if sal > 1250.00:
    sal2 = sal + (sal * (10/100))
else:
    sal2 = sal + (sal * (15/100))

print(f'Quem ganha {sal:.2f}, passará a ganhar {sal2:.2f} agora!')