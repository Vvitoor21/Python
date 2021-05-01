pessoas_festa = ['Rogerio', 'Paula', 'Carolina', 'Anderson', 'Felipe', 'Marcos', 'Bruna']
pessoas_festa.sort()# Uma ordem crescente
print(pessoas_festa)
pessoas_festa.sort(reverse=True)# Uma ordem decrescente
print(pessoas_festa)
pessoas_festa.sort()
print(pessoas_festa)
numeros = [1, 5, 4, 7, 8, 2]
print(f'Numeros ordenados temporariamente:{sorted(numeros)}')
print(f'Numeros desordenados:{numeros}')
numeros.reverse()
print(f'Numeros revertidos: {numeros}')

lugares_mundo = ['Rio', 'França', 'Nova York', 'Londres', 'Madri']
print(f'\nLugares que eu gostaria de visitar:{lugares_mundo}')
print(sorted(lugares_mundo))
print(f'Exibindo lista original novamente: {lugares_mundo}')
print(sorted(lugares_mundo, reverse=True))# Ordem alfabetica inversa.
print(lugares_mundo) # Lista normal
lugares_mundo.reverse()# Lista de tras para frente sem ordem alfabetica.
print(lugares_mundo)
lugares_mundo.reverse()# Lista voltando para a ordem normal.
print(lugares_mundo)
lugares_mundo.sort() # Ordenade em ordem alfabética.
print(lugares_mundo)
lugares_mundo.sort(reverse=True)
print(lugares_mundo) #Ordem alfabetica inversa.

print(f'Quantidade de cidades: {len(lugares_mundo)}')

print(lugares_mundo[-2])

cores = []
opcoes = ''

while opcoes != 'sair':
    opcoes = input()
    cores.append(opcoes)
    if opcoes == 'sair':
        cores.remove('sair')
print(cores)



