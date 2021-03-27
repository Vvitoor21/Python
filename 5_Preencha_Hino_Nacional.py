print('De acordo com o site da Terra:\n58,4% dos brasileiros não sabem cantar o hino nacional')

print('Você consegue acertar as palavras com esse teste ? \n')

#Atividade para treinamento do Loop WHILE

nome1= 'plácidas'
nome2='retumbante'
nome3='fúlgidos'
nome4='instante'

nome5= 'penhor'
nome6 = 'braço'
nome7 = 'liberdade'
nome8 = 'desafia'

musica=''

while musica !=  nome1:
    musica=input('Ouviram do ipiranga as margens: ')
    if musica != nome1:
        print('errado')

while musica != nome2:
    musica = input('De um povo heróico o brado: ')
    if musica != nome2:
        print('errado')

while musica != nome3:
    musica = input('E o sol da liberdade em raios: ')
    if musica != nome3:
        print('errado')

while musica != nome4:
    musica = input('Brilho no céu da pátria nesse: ')
    if musica != nome4:
        print('errado')

while musica != nome5:
    musica = input('Se o "?" dessa igualdade: ')
    if musica != nome5:
        print('errado')

while musica != nome6:
    musica = input('Conseguimos conquistar com " ? " forte, : ')
    if musica != nome6:
        print('errado')

while musica != nome7:
    musica = input('Em teu seio, ó : ')
    if musica != nome7:
        print('errado')

while musica != nome8:
    musica = input('" ? " o nosso peito a própria morte! : ')
    if musica != nome8:
        print('errado')

print('Letra com as respostas corretas : \n')

print(f'\n0uviram do ipiranga as margens {nome1}.')
print(f'De um povo heroico o brado {nome2},')
print(f'E o sol da liberdade em raios {nome3},')
print(f'Brilhou no céu da pátria nesse {nome4}.\n')

print(f'Se o {nome5} dessa igualdade')
print(f'Conseguimos conquistar com {nome6} forte,')
print(f'Em teu seio, ó {nome7},')
print(f'{nome8} o nosso peito a própria morte!\n')

print('Ó Patria amada,')
print('Idolatrada,')
print('Salve! Salve!\n')