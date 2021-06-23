months={'Jan':'January','Feb':'February','Mar':'March','Apr':'April'}
print('O dicionario completo é:')
print(months)

print('Os valores do dicionario são:')
print(months.values())

print('As chaves dos dicionarios são:')
print(months.keys())

months['Ma']='May'
months['Ju']='June'
months['Jul']='July'

print(months)

months['JAN'] =months['Jan']
del months['Jan']

print(months)
print(months.items())

dict = { 'a': 10, 'b':20, 'c':30}

letras =['a','b','c','d']
numeros =[5 , 10, 15, 20]

dados_dic = dict(letras,numeros)

dict.update({'a':100,'e':25})

dadosCopy = dict.copy()

dict.clear()
