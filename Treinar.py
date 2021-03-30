print("PARTICIPANTES DO REALITY SHOW")

import  time

time.sleep(2)
print('SEJA BEM VINDO AO PROCESSO DE SELEÇÃO')
time.sleep(2)
print('Antes de começarmos, precisamos de algumas informações a seu respeito')
print('Informe nome:')
nome = str(input())
print('Informe idade')
idade = int(input())
print('Informe sua profissao')
prof = input()

class Usuario:
    def __init__(self):
        self.nome = nome
        self.idade = idade
        self.profissao = prof

    def mostra_informacoes(self):
        print(self.nome, str(self.idade)+' anos',' profissao: '+ self.profissao)

    def __repr__(self):
        return str(self.__dict__)

class Pessoa2:
    def __init__(self):
        self.nome = 'Amanda'
        self.idade = 29
        self.profissao = 'Engenheira'

    def mostra_informacoes(self):
        print(self.nome, str(self.idade)+' anos',' profissao: '+ self.profissao)

    def __repr__(self):
        return str(self.__dict__)

class Pessoa3:
    def __init__(self):
        self.nome = 'Arthur'
        self.idade = 41
        self.profissao = 'Administrador'

    def mostra_informacoes(self):
        print(self.nome, str(self.idade)+' anos',' profissao: '+ self.profissao)

    def __repr__(self):
        return str(self.__dict__)

class Pessoa4:
    def __init__(self):
        self.nome = 'Paula'
        self.idade = 29
        self.profissao = 'Arquiteta'

    def mostra_informacoes(self):
        print(self.nome, str(self.idade)+' anos',' profissao: '+ self.profissao)

    def __repr__(self):
        return str(self.__dict__)

usuario = Usuario()

time.sleep(2)
print(f'Muito prazer {usuario.nome}. Você tem {usuario.idade} anos  e trabalha como {usuario.profissao}. Muito bom!!! Aqui abaixo esta as informacoes dos outros 4 participantes')

print('----------------------------------------------------------------------------------')

amanda = Pessoa2()
arthur = Pessoa3()
paula = Pessoa4()

time.sleep(6)
print('LISTA DE PARTICIPANTES : ')

lista = [ amanda.nome, arthur.nome, paula.nome, usuario.nome]
print(lista)
time.sleep(2)
print('PRINCIPAIS INFORMACOES')
time.sleep(2)
amanda.mostra_informacoes()
time.sleep(2)
arthur.mostra_informacoes()
time.sleep(2)
paula.mostra_informacoes()
time.sleep(2)
usuario.mostra_informacoes()

time.sleep(2)
print('CONTAGEM REGRESSIVA: ')

for n in range(10, -1, -1):
    time.sleep(1)
    print(n)

frase = "BIG BROTHER BRASIL"

import sys

for i in list(frase):
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.25)

time.sleep(2)
print('\nProva do lider!!!')
time.sleep(2)
print('Todos jogam nessa rodada')

for i in 'PERGUNTA:':
    print(i, end='')
    time.sleep(0.40)

import random

resp = input('\nQuantos animais de cada espécie, Moisés colocou em sua arca: 1, 2 ou 3? DIGITE O NUMERO')

if resp == 0:
    print('VOCCÊ É O LIDER !!!!')
else:
    for i in 'NÃO FOI MOISES QUEM CONSTRUIU A ARCA. VOCE ERROU...':
        print(i, end='')
        time.sleep(0.10)
    escolhido = random.choice(lista)
    time.sleep(2)
    print(f'\nO LIDER É: {escolhido}')
    lista.remove(escolhido)
    time.sleep(2)
    print(f'\nESTÃO NO PAREDÃO: {lista}')
    lista.remove(random.choice(lista))
    time.sleep(2)
    print(f'\nVoltaram :{lista}')

lista.append(escolhido)
print(f'\nJOGAM A FINAL: {lista}')

time.sleep(5)
print('\nPESSOAS ESTÃO VOTANDO...')
for n in range(20,10,-1):
    time.sleep(1)
    print(n)
print('\nVOTAÇÃO ENCERRADA...')
time.sleep(5)
print('FAZENDO A CONTAGEM DOS VOTOS...')
for n in range(10,0,-1):
    time.sleep(1)
    print(n)

for l in 'O VENCEDOR É : : : : : : : : :':
    print(l, end='')
    time.sleep(0.25)
vencedor = random.choice(lista)

print(f'\n{vencedor} !!!!! PARABÉNS. 1,5 MILHÕES DE REAIS !!!')













