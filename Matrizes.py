import numpy as np
print('Matrizes são arrays bidimensionais. ')

a = np.array([[1,2,3],[1,2,3]])
print(a)
print(a.shape)
print(a.dtype)

lista = [[0,0,0],[1,1,1],[2,2,2]]
m= np.matrix(lista)
print(m)

m[0,0]=10
m[0,1]=20
m[0,2]=30
m[1,0]=40
m[1,1]=50
m[1,2]=60
m[2,0]=70
m[2,1]=80
m[2,2]=90

print(m)

print(m.shape)

x = np.array([10,20])  # Tipos de dados do tipo int.
y = np.array([1.0,2,0]) # Tipos de dados do tipo float.
z = np.array([1,2,3], dtype = np.float64) # Alterando o tipo dos elementos.
