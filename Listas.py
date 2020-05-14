friends = ['Harry' ,' Steve ', 'Tony']
#    Indexes  0        1         2
print(friends)
print(friends[0])# imprimindo o primeiro nome da lista.
friends.append('Geralt')#append Coloca dados na lista'.
print(friends)
friends.insert(1,'Peter')#Comando "insert" necessita colocar dados em um índice especifico.
print(friends)
friends.remove('Harry')#Comando remove "remmove" dados da lista.
print(friends)
#friends.clear() Coloquei clear como comentario pois estecomando limpa a lista deixando-a vazia.
# print(friends)
print('Qual a posição do nome Geralt? ')
print(friends.index('Geralt'))# Comando index mostra o índice do dado especificado.

numeros=[1,2,3,4,5,6,7,8,9]
#Indexes 0 1 2 3 4 5 6 7 8
print(numeros)
print(numeros[1:9:2])

import random # é necessario importar a bblioteca random para deixar os valores da lista aleatórios com o método shuffle().

random.shuffle(numeros)
print(numeros)

friends.extend(numeros)
print(friends)
numeros.pop() # Comando pop(). elimina o último dado.
print(numeros)

conta=[0,1,2,3]
conta.reverse() # Comando reverse inverte a lista.
print(conta)

