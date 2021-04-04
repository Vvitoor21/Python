import time
import sys
#Teste versionamento de cod

print('OLÁ USUÁRIO')
time.sleep(2)
print('SEJA BEM VINDO A ESTE PROGRAMA')
time.sleep(2)
print('ESTÁ PRONTO PARA EMBARCAR NESSA JORNADA???')
time.sleep(2)

print('Você precisara digitar informações importantes ao seu respeito...deseja continuar?')

print('Digite 1 para "sim" e 2 para "não".')

numero=int(input('Escolha :'))
if numero == 1 :
    print('O programa será inicializado em instantes...')
    time.sleep(3)
    print('Tudo OK!!!')
else:
        print('Programa está sendo finalizado em 3...')
        time.sleep(1)
        print('2...')
        time.sleep(1)
        print('1...')
        time.sleep(1)
        print('O PROGRAMAA FOI ENCERRADO :(')
        sys.exit()

nome = input('Digite o seu primeiro nome: ')
sobrenome = input('Digite o seu sobrenome: ')
ano = int(input('Precisamos calcular a sua idade.Por favor digite o ano que você nasceu: '))
idade = 2020 - int(ano)
print(f'Seja bem vindo {nome} {sobrenome}. Calculamos que você tem {idade} anos de idade e está autorizada a começar.')