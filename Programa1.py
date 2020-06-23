import time
import sys

for n in range (1):
    print('OLÁ USUÁRIO')
    time.sleep(3)
    print('SEJA BEM VINDO AO MEU PROGRAMA')
    time.sleep(3)
    print('ESTÁ PRONTO PARA EMBARCAR NESSA JORNADA???')
    time.sleep(3)

print('Você precisara digitar informações importantes ao seu respeito...deseja continuar?')

print('Digite 1 para "sim" e 2 para "não".')

numero=int(input('Escolha :'))
if numero == 1 :
    print('O programa será inicializado em instantes...')
    time.sleep(3)
    print('Tudo OK!!!')
else:
    for n in range(1):
        print('Programa está sendo finalizado em 3...')
        time.sleep(3)
        print('2...')
        time.sleep(3)
        print('1...')
        time.sleep(3)
        print('O PROGRAMAA FOI ENCERRADO :(')
        sys.exit()

nome = input('Digite o seu primeiro nome: ')
sobrenome = input('Digite o seu sobrenome: ')
ano = int(input('Precisamos calcular a sua idade.Por favor digite o ano que você nasceu: '))
idade = 2020 - int(ano)
print(f'Seja bem vindo {nome} {sobrenome}.Calculamos que você tem {idade} anos de idade e está autorizada a começar.')
print (f'Diga o nome de pessoas que você gosta( é necessário nome e sobrenome: .Para encerrar digite "sair" .')

lista=[]
pessoas=''

print('Informe o nome: ')

while pessoas != 'sair':
    pessoas=input()
    if pessoas != 'sair':
        lista.append(pessoas)

print(f'A lista de pessoas que você tem consideração tem {len(lista)} nomes: {lista}')

print('FIM DO PROGRAMA -- Obrigado!!')
