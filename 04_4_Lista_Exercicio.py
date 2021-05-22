pizzas = ['Camarão', 'Mussarela', 'Portuguesa']
for pizza in pizzas:
    print(pizza.title())

print(f'\n')

for indice, pizza in enumerate(pizzas):
    print(f'{indice+1}° pizza desejada: {pizza}')

if len(pizzas) >=3:
    print('\nEu realmente gosto de comer pizza\n')

animais = ['cachorro','pato','cobra']

for animal in animais:
    print(f'{animal.title()} é um dos meus animais de estimação')