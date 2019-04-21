from time import  sleep
num = int(input('Digite um número par ver sua tabuada: '))

for i in range(1, 11):
    print(f'{num} X {i} = {num * i}')
    sleep(1)