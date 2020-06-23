print('-----INICIANTE-----')

nome = "Vitor"
idade = 21
print(f'Meu nome é {nome} e eu teno {idade} anos.')

print('Steve\nRogers')# \n realiza a quebra de linha.
print('Tony Stark')

titulo = 'Os Vingadores'
print('O filme "'+titulo + '" é muito legal.')
print(titulo.upper().isupper()) # titulo.title().istitle() é possível ultilizar dois métodos em uma linha.
print(len(titulo)) #len(). é usado para contar quantos indices possuem a String
print(titulo[0])
print(titulo[0:8])
print(titulo[5])
print(titulo.index('O'))
print(titulo.replace('Vingadores','Programadores'))# replace() necessita coloca dois valores para efetuar atroca de dados.

print(10 % 3) # % calcula o resto da divisão
n = 10
n = str(n)
print(type(n))
print(int(n))
print(type(n))

numero = -7
print(abs(numero)) # o comando abs() deixa o numero negativo em positivo.
print(pow(7,2)) # o comando pow() faz a potenciação com dois dados.
print(max(7,2)) # max() compara o valor de dois dados para saber qual será o maior.
print(min(7,2)) # min() compara o valor de dois qados para saber qua será o menor.
print(round(5.754)) # round() arredonda o valor de um némero decimal.

from math import * #importa funções matamáticas da biblioteca Math.A biblioteca Math possuem funções espefíficas a serem implantadas.


print(ceil(3.7))  #arredonda o numero          ceil().
print(sqrt(36))   #calcula a raiz quadrada sqrt().

name = input('Enter your name: ')
lastname = input('Enter your lastname: ')
print(f'You´re welcome {name} {lastname}.')

color = input('Enter a color: ')
noun = input('Enter a noun: ')
people = input('Enter a people: ')

print(f'Roses are {color}.')
print(f'{noun} are blue.')
print(f'I love {people}.')
