print('Crie a lista de funcionários da empresa: ')

recepcao=[]#recepcao é uma lista vazia
funcionarios=''#funcionarios ira receber strings

print("Digite o nome do recepcionista ou 'sair' para sair")

while funcionarios != 'sair':
    funcionarios=input()
    if funcionarios != 'sair':
        recepcao.append(funcionarios)

print('A lista dos funcionarios da Recepção é :')
print(recepcao)
