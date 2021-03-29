
print("PARTICIPANTES DO REALITY SHOW")
print( '- - - ATENÇÃO PARA ALGUNS COMANDOS DURANTE O PROCESSO - - - !!!')

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

class Pessoa:
    def __init__(self):
        self.nome = 'Vitor'
        self.idade = 22
        self.profissao = 'Programador'

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

vitor = Pessoa()
amanda = Pessoa2()
arthur = Pessoa3()
paula = Pessoa4()

time.sleep(6)
print('LISTA DE PARTICIPANTES : ')

lista = [ vitor.nome, amanda.nome, arthur.nome, paula.nome,usuario.nome ]
print(lista)
time.sleep(2)
print('PRINCIPAIS INFORMACOES')
time.sleep(4)
vitor.mostra_informacoes()
time.sleep(4)
amanda.mostra_informacoes()
time.sleep(4)
arthur.mostra_informacoes()
time.sleep(4)
paula.mostra_informacoes()
time.sleep(4)
usuario.mostra_informacoes()

time.sleep(2)
print('O PROCESSO SERÁ INICIADO EM: ')

for n in range(10, -1, -1):
    time.sleep(1)
    print(n)

frase = "BIG BROTHER BRASIL"

import sys

for i in list(frase):
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.25)