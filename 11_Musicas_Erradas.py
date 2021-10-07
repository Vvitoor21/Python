print('Ivete Sangalo: "Arerê! .... .... .... love com você"')

print('Qual opção completa a musica? ')
print('1 -> Arerê! Um love, love, love com você')
print('2 -> Arerê! Um lobby, um hobby,um love com você')

resp = int(input('Digite sua opção: '))

while resp != 1 and resp != 2:
    resp = int(input('Resposta invalida. Digite novamente: '))
if resp == 2:
    print('Arerê! Um lobby, um hobby,um love com você. Voce acertou :D ')
if resp == 1:
    print('Parabéns. Você conseguiu errar a música da Ivete Sangalo. Esta não é a resposta certa.')


print('Cássia Eller: Quem sabe o príncipe virou um ....., que vive dando no meu saco…')
print('Qual opção completa a musica? ')
print('1 -> virou um sapo')
print('2 -> virou um chato')

resp2 = int(input('Digite sua opção: '))

while resp2 != 1 and resp2 != 2:
    resp2 = int(input('Resposta invalida. Digite novamente: '))
if resp2 == 2:
    print('Quem sabe o príncipe virou um chato, que vive dando no meu saco…. Voce acertou :D ')
if resp2 == 1:
    print('O principe virou um chato e não um sapo denovo. Esta não é a resposta certa.')