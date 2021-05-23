for value in range(1, 5):
    print(value)

numbers = list(range(1,11))
print(numbers)

numeros_pares = list(range(0,11,2))
print(numeros_pares)

squares = [ ]
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

digitos = [2,52,63,5,4,289,66,2,4,1,223,8,7,1,5,2]
print(min(digitos))

print(max(digitos))

print(sum(digitos))

list_comp = [ valor+10 for valor in range(0, 101, 10)]
list_comp.remove(110)
print(list_comp)

for value in range(1, 5):
    print(str(value)+'---'+str(value+1))
    
for value in range(1, 21):
    print(value)

#for num in range(0, 1000001):
 #   print(num)

lista = list(range(0,1000001))
#print(lista)
print(min(lista))
print(max(lista))
print(sum(lista))

for n in range(3,31,3):
    print(n)
# multiplos de 3

for c in range(1,11):
    print(c**3)
# elevado ao cubo

lista = [a**3 for a in range(1,11)]
print(lista)
