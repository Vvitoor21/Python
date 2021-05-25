# Removendo com o método pop()
materias = ['biologia', 'matematica', 'portugues', 'fisica', 'quimica', 'artes']
print(materias)
materias_pop = materias.pop()
print(materias_pop)  # .pop(0), .pop(1), etc...

# Removendo de acordo com o valor
print(materias)
materias.remove('biologia')
print(materias)
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

"""
MÉTODO ERRADO PARA ENUMERAR INDICES

pessoas_jantar = ['Vitor', 'Marcela', 'Gabriel', 'Bruno', 'Tais']
final = len(pessoas_jantar)

for index in range(1, final+1):
    for pessoa in pessoas_jantar:
        print(index, pessoa)
"""
pessoas_jantar = ['Vitor', 'Marcela', 'Gabriel', 'Bruno', 'Tais']

for indice, pessoa in enumerate(pessoas_jantar): # Lembrar do indice e metodo = enumerate ao enumerar(enumerate) os indices com os valores.
    print(f'{indice+1}° Pessoa: {pessoa}, você foi convidado(a) para o jantar.')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print(f'A {indice-1}º pessoa: {pessoas_jantar.pop(2)}, não podera comparecer.')
# Adicionando um novo convidado:
pessoas_jantar.insert(2, 'Rafaela')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print(f'Nova lista de convidados: {pessoas_jantar}')
pessoas_jantar.insert(6, 'Mayara')
pessoas_jantar.insert(7, 'Tiago')
pessoas_jantar.append('Rodolfo')
print(pessoas_jantar)

for indice, pessoa in enumerate(pessoas_jantar):
    print(f'{indice+1}°, {pessoa}. O jantar especial será amanhã.')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('Apenas duas pessoas para o jantar:')


print(len(pessoas_jantar))

while len(pessoas_jantar) <= 8:
    pessoas_jantar.pop()
    if len(pessoas_jantar) <= 2: # Removendo todas as pessoas da lista de tras pra frente ate sobras os ultimos 2.
        break

print(f'O encontro será entre: {pessoas_jantar[0]} e {pessoas_jantar[1]}')
del pessoas_jantar[1]  # O parâmetro elimina a quantidade.

print(f'Só esteve presente: {pessoas_jantar[0]}')

list = ['a', 'b', 'a', 'c']

list = [9 if i =='a' else i for i in list]

print(list)
