'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

peso = float(input('Qual é o sel peso (kg): '))
altura = float(input('Qual é a sua altura (m):'))
imc = peso / altura ** 2

print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print('Você esta ABAIXO DO PESO normal')
elif imc < 25:
    print('Você esta no PESO IDEAL')
elif imc < 30:
    print('Você esta com SOBREPESO')
elif imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você esta com OBESIDADE MORBIDA')