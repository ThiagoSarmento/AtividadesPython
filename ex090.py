aluno = {}

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a media de {aluno["nome"]} '))
if aluno['media'] < 7.5:
    aluno['situacao'] = 'reprovado'
else:
    aluno['situacao'] = 'aprovado'

print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["media"]}')
print(f'A situação é igual a {aluno["situacao"]}')