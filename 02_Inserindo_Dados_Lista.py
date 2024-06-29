print('Crie a lista de funcionários da empresa: ')

recepcao=[] #recepcao é uma lista vazia
funcionarios = '' # funcionarios ira receber strings

print("Digite o nome do funcionario e depois 'sair' para sair")

while funcionarios != 'sair':
    funcionarios=input()
    if funcionarios != 'sair':
        recepcao.append(funcionarios)

print('A lista dos funcionarios são:')
print(recepcao)
