nome1= 'plácidas'
nome2='retumbante'
nome3='fúlgidos'
nome4='instante'

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

print(f'0uviram do ipiranga as margens {nome1}.')
print(f'De um povo heroico o brado {nome2}.')
print(f'E o sol da liberdade em raios {nome3}.')
print(f'Brilhou no céu da pátria nesse {nome4}.')
