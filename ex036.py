'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o valor do salário: '))
ano = int(input('Em quantos anos deseja pagar: '))

prestacao = casa / (ano * 12)
limite = salario * (30/100)

if limite >= prestacao:
    print('Emprestimo APROVADO')
elif prestacao > limite:
    print('Emprestimo NEGADO')

print(f'Para pagar uma casa no valor de R${casa:.2f} \n'
      f'em {ano} anos, a prestação será de R${prestacao:.2f}\n'
      f'e você possui um limite de R${limite:.2f} para prestações.')