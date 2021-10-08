import time

print('Ivete Sangalo: "Arerê! .... .... .... love com você"')
time.sleep(5)
print('Qual opção completa a musica? ')
time.sleep(5)
print('1 -> Arerê! Um love, love, love com você')
time.sleep(3)
print('2 -> Arerê! Um lobby, um hobby,um love com você')
time.sleep(4)
resp = int(input('Digite sua opção: '))

while resp != 1 and resp != 2:
    resp = int(input('Resposta invalida. Digite novamente: '))
if resp == 2:
    print('Arerê! Um lobby, um hobby,um love com você. Voce acertou :D ')
if resp == 1:
    print('Parabéns. Você conseguiu errar a música da Ivete Sangalo. Esta não é a resposta certa.')

time.sleep(7)
print('Cássia Eller: Quem sabe o príncipe virou um ....., que vive dando no meu saco…')
time.sleep(5)
print('Qual opção completa a musica? ')
time.sleep(5)
print('1 -> virou um sapo')
time.sleep(3)
print('2 -> virou um chato')
time.sleep(4)
resp2 = int(input('Digite sua opção: '))

while resp2 != 1 and resp2 != 2:
    resp2 = int(input('Resposta invalida. Digite novamente: '))
if resp2 == 2:
    print('Quem sabe o príncipe virou um chato, que vive dando no meu saco…. Voce acertou :D ')
if resp2 == 1:
    print('O principe virou um chato e não um sapo denovo. Esta não é a resposta certa.')

time.sleep(7)
print('Pitty: Pense, fale, compre, beba, leia, vote, não se esqueça....')
time.sleep(5)
print('Qual opção completa a musica? ')
time.sleep(5)
print('1 -> Use, seja, ousadia…')
time.sleep(3)
print('2 ->Use, seja, ouça, diga…')
time.sleep(4)
resp3 = int(input('Digite sua opção: '))

while resp3 != 1 and resp2 != 2:
    resp3 = int(input('Resposta invalida. Digite novamente: '))
if resp3 == 2:
    print('Parabéns. Resposta correta')
if resp3 == 1:
    print('Nade de ousadia nessa música. A resposta esta errada.')

time.sleep(7)
print('Pitty: Pense, fale, compre, beba, leia, vote, não se esqueça....')
time.sleep(5)
print('Qual opção completa a musica? ')
time.sleep(5)
print('1 -> Use, seja, ousadia…')
time.sleep(3)
print('2 ->Use, seja, ouça, diga…')
time.sleep(4)
resp3 = int(input('Digite sua opção: '))

while resp3 != 1 and resp2 != 2:
    resp3 = int(input('Resposta invalida. Digite novamente: '))
if resp3 == 2:
    print('Parabéns. Resposta correta')
if resp3 == 1:
    print('Nade de ousadia nessa música. A resposta esta errada.')
