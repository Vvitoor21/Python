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
