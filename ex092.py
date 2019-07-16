from datetime import date
dados = {}

nome = str(input('Digite o nome: '))
anoNasc = int(input('Digite o ano de nascimento: '))
ctps = int(input('Número da CTPS: '))
# obtendo a idade
hoje = date.today().year
idade = hoje - anoNasc

dados['nome'] = nome
dados['idade'] = idade
dados['ctps'] = ctps

# se tiver ctps
if ctps != 0:
    anoCont = int(input('Ano de contratação: '))
    sal = float(input('Salário: '))
    # obtendo aposentadoria
    anoAps = anoCont + 35
    idadeAps = anoAps - anoNasc
    dados['contratação'] = anoCont
    dados['salário'] = sal
    dados['aposentadoria'] = idadeAps

print('=' * 40)
print(dados)
print()

for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
