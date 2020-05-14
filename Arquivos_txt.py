arquivo = open('estudos.txt','r',encoding='utf8')

print(arquivo.read())

arquivo.seek(0) # Retorna o ponteiro para c começo novamente.


print(arquivo.readline())# Lê a primeira linha.
print(arquivo.readline())# Lê a segunda linha.
print(arquivo.readline())# Lê a terceira linha.

arquivo.close() # Fechando arquivo.
