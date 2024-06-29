#Criando uma Calculadora

num = int(input('Digite um número para saber o resultado na calculadora: '))

print(f'TABUADA DO NÚMERO {num}.')

print(f'{num} * 1  : {num * 1}')
print(f'{num} * 2  : {num * 2}')
print(f'{num} * 3  : {num * 3}')
print(f'{num} * 4  : {num * 4}')
print(f'{num} * 5  : {num * 5}')
print(f'{num} * 6  : {num * 6}')
print(f'{num} * 7  : {num * 7}')
print(f'{num} * 8  : {num * 8}')
print(f'{num} * 9  : {num * 9}')
print(f'{num} * 10 : {num *10}')

#WHILE

num = int(input('Digite um número para saber o resultado na calculadora: '))

n = 0

while n <= 10:
    print(f'{n} x {num} = {n*num}')
    n = n + 1
