'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
t1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))


for cont in range(1, 11):
    print(f'{t1} -> ', end='')
    t1 += r

print('Acabou!')