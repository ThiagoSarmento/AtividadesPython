'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

med = (n1 + n2) / 2

print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {med:.1f}')

if med < 5:
    print('Aluno REPROVADO!')
elif med >= 5 and med < 7:
    print('Aluno em RECUPERAÇÃO!!')
else:
    print('Aluno APROVADO!!!')
