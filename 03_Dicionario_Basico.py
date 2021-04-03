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
