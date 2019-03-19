'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

print(f'{"LOJAS GUNABARA":=^40}')

compras = float(input('Preço das compras R$: '))

print('''
FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
valida = False
while valida == False:
    opcao = input('Qual é a opção: ')
    try:
        opcao = int(opcao)
        if opcao >= 1 and opcao <= 4:
            valida = True
        else:
            print('Opção inválida! Escolha outra opção!!')
    except:
        print('Opção inválida! Escolha outra opção!!')
        continue

if opcao == 1:
    final = compras * (1 - 10/100)
    print(f'Sua compra de R${compras:.2f} vai custar R${final:.2f} com 10% de desconto!')
elif opcao == 2:
    final = compras * (1 - 5/100)
    print(f' Sua compra de R${compras:.2f} à vista no cartão vai custar R${final:.2f}')
elif opcao == 3:
    parcela = compras / 2
    print(f'Sua compra de R${compras:.2f} será parcelada em 2x de R${parcela:.2f} sem juros')
elif opcao == 4:
    num = int(input('Quantas parcelas: '))
    final = compras * (1 + 20/100)
    parcela = final / num
    print(f'Sua compra será parcelada em {num} de R${parcela:.2f} com juros.\n'
          f'Sua compra de R${compras:.2f} vai custar R${final:.2f} no final!')
