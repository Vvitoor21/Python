"""
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

# --------------------------------------------------------------------------------------------------------------

class Usuario:
    def __init__(self):
        self.nome = nome
        self.idade = idade
        self.profissao = prof

    def mostra_informacoes(self):
        print(self.nome, str(self.idade)+' anos',' profissao: '+ self.profissao)

    def __repr__(self):
        return str(self.__dict__)

class Pessoa1:
    def __init__(self):
        self.nome = 'Felipe'
        self.idade = 29
        self.profissao = 'Professor'

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

class Pessoa5:
    def __init__(self):
        self.nome = 'Priscila'
        self.idade = 37
        self.profissao = 'Veterinaria'

    def mostra_informacoes(self):
        print(self.nome, str(self.idade)+' anos',' profissao: '+ self.profissao)

    def __repr__(self):
        return str(self.__dict__)

# ---------------------------------------------------------------------------------------------------------

usuario = Usuario()

time.sleep(2)
print(f'Muito prazer {usuario.nome}. Você tem {usuario.idade} anos  e trabalha como {usuario.profissao}. Muito bom!!! Aqui abaixo estão as informações dos outros participantes')

print('----------------------------------------------------------------------------------')

felipe = Pessoa1()
amanda = Pessoa2()
arthur = Pessoa3()
paula = Pessoa4()
priscila = Pessoa5()

time.sleep(10)
print('LISTA DE PARTICIPANTES : ')
lista = [ felipe.nome, amanda.nome, arthur.nome, paula.nome, priscila.nome, usuario.nome]
print(lista)

time.sleep(2)
print('PRINCIPAIS INFORMAÇÕES ')
time.sleep(3)
felipe.mostra_informacoes()
time.sleep(2)
amanda.mostra_informacoes()
time.sleep(2)
arthur.mostra_informacoes()
time.sleep(2)
paula.mostra_informacoes()
time.sleep(2)
priscila.mostra_informacoes()
time.sleep(2)
usuario.mostra_informacoes()

time.sleep(4)
print('CONTAGEM REGRESSIVA PARA INÍCIO DO PROGRAMA : ')

for n in range(10, -1, -1):
    time.sleep(1)
    print(n)

frase = "* * * BIG BROTHER BRASIL * * *"

import sys

for i in list(frase):
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.25)

time.sleep(2)
print('\nProva do lider!!!')
time.sleep(2)
print('Todos jogam nessa rodada')

for i in ' - - - 1° PERGUNTA - - - :':
    print(i, end=' ')
    time.sleep(0.40)

import random

print('\nQuantos animais de cada espécie, Moisés colocou em sua arca: 1, 2 ou 3? DIGITE O NUMERO: ')

resp = int(input())

if resp == 0:
    time.sleep(3)
    print('VOCÊ É O LIDER DA RODADA !!!!\n')
    lista.remove(usuario.nome)
    eliminado = random.choice(lista)
    time.sleep(3)
    print(f'O PAREDÃO ESTÁ ENTRE: {lista}\n')
    lista.remove(eliminado)
    lista.append(usuario.nome)
    time.sleep(6)
    print(f'O ELIMANDO FOI: {eliminado}')

else:
    for i in 'NÃO FOI MOISES QUEM CONSTRUIU A ARCA. VOCE ERROU...':
        print(i, end='')
        time.sleep(0.10)
    lista.remove(usuario.nome)
    escolhido = random.choice(lista)
    time.sleep(2)
    print(f'\nO LIDER É: {escolhido}')
    lista.remove(escolhido)
    lista.append(usuario.nome)
    time.sleep(2)
    print(f'\nESTÃO NO PAREDÃO: {lista}')
    lista.remove(usuario.nome)
    lista.remove(random.choice(lista))
    lista.append(usuario.nome)
    time.sleep(2)
    print(f'O Eliminado foi : {escolhido}')
    print(f'\nVoltaram :{lista}')
    lista.append(escolhido)

time.sleep(3)
print(f'SEGUEM NO JOGO: {lista}')

for i in ' - - - 2° PERGUNTA - - - : \n':
    print(i, end=' ')
    time.sleep(0.40)

time.sleep(2)
print('ATENÇÃO\n')

time.sleep(2)
print('No dia 7 de setembro, nós comemoramos o Dia da Independência no Brasil.'
      'Em Portugal, também existe 7 de setembro ??? \n')

time.sleep(7)
print('DIGITE 1 PARA SIM E 2 PARA NÃO')
dia = int(input())

if dia == 1:
    print('Você é esperto. E agora é o líder !!!')
    time.sleep(3)
    print('Vamos deixar os proximos  participantes enfrentarem o paredão...')
    lista.remove(usuario.nome)
    eliminado2 = random.choice(lista)
    time.sleep(3)
    print(f'O PAREDÃO ESTÁ ENTRE: {lista}\n')
    lista.remove(eliminado2)
    lista.append(usuario.nome)
    time.sleep(3)
    print(f'O ELIMANDO FOI: {eliminado2}')
else:
    for i in ' Claro que sim, bem como nos Estados Unidos, na Espanha, na Austrália... '\
             'Basta olhar o calendário desses países e reparar que 7 de setembro estará lá, assim como todos os outros dias do ano\n':
        print(i, end='')
        time.sleep(0.10)

    time.sleep(5)
    print('VOCÊ ERROU !!!! ')
    lista.remove(usuario.nome)
    escolhido2 = random.choice(lista)
    time.sleep(2)
    print(f'\nO LIDER É: {escolhido2}')
    lista.remove(escolhido2)
    lista.append(usuario.nome)
    time.sleep(2)
    print(f'\nESTÃO NO PAREDÃO: {lista}')
    lista.remove(usuario.nome)
    lista.remove(random.choice(lista))
    lista.append(usuario.nome)
    time.sleep(2)
    print(f'\nVoltaram :{lista}\n')
    lista.append(escolhido2)
    print('TEM SORTE DE AINDA NÃO TER SIDO ELIMINADO')

time.sleep(3)
print(f'SEGUEM NO JOGO:{lista}')

for n in ' - - - 3° E ÚLTIMA PERGUNTA - - - \n':
    print(n, end=' ')
    time.sleep(0.10)

import random
time.sleep(2)
print('\nA mãe de Mário tem três filhos. O primeiro se chama Março e o segundo se chama Abril. Qual é o nome do terceiro ?')
print('Digite 1 - Junho, 2 - Mário, 3 - Maio , 4 - Fevereiro')

nome = int(input())

while nome not in (1, 2, 3, 4):
    print('Não entendi..Digite Novamente')
    nome = int(input())
if nome == 2:
    print('ACERTOU !!!')
    time.sleep(3)
    print('Vamos deixar os proximos 3 participantes enfrentarem o paredão...')
    lista.remove(usuario.nome)
    eliminado3 = random.choice(lista)
    time.sleep(3)
    print(f'O PAREDÃO ESTÁ ENTRE: {lista}\n')
    lista.remove(eliminado3)
    lista.append(usuario.nome)
    time.sleep(3)
    print(f'O ELIMANDO FOI: {eliminado3}')
if nome in(1,3,4):
    for n in 'A prória pergunta já diz a resposta...." A mãe de Mário tem três filhos. O primeiro se chama Março e o segundo se chama Abril\n" ':
        print(n, end=' ')
        time.sleep(0.10)
    time.sleep(3)
    print('OBVIAMENTE O 3° É MARIO. VOCÊ ERROU !!!! ')
    lista.remove(usuario.nome)
    escolhido3 = random.choice(lista)
    time.sleep(2)
    print(f'\nO LIDER É: {escolhido3}')
    lista.remove(escolhido3)
    lista.append(usuario.nome)
    time.sleep(2)
    print(f'\nESTÃO NO PAREDÃO: {lista}')
    lista.remove(usuario.nome)
    lista.remove(random.choice(lista))
    lista.append(usuario.nome)
    time.sleep(2)
    print(f'\nVoltaram :{lista}\n')
    lista.append(escolhido3)

quit()

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

lista.remove(usuario.nome)
for l in ' O VENCEDOR É : : : : : : : : ':
    print(l, end=' ')
    time.sleep(0.25)
vencedor = random.choice(lista)
##
time.sleep(4)
print(f'\n{vencedor} !!!!! PARABÉNS. 1,5 MILHÕES DE REAIS !!!')


def acerto():
    time.sleep(3)
    print('VOCÊ É O LIDER DA RODADA !!!!\n')
    lista.remove(usuario.nome)
    eliminado = random.choice(lista)
    time.sleep(3)
    print(f'O PAREDÃO ESTÁ ENTRE: {lista}\n')
    lista.remove(eliminado)
    lista.append(usuario.nome)
    time.sleep(6)
    print(f'O ELIMANDO FOI: {eliminado}')

print(" - - - INFORMAÇÕES DE ENTRADA PARA O REALITY SHOW - - - ")

import pandas as pd
"""
def prova1():
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

    print('---------HINO NACIONAL---------')
    print(f'0uviram do ipiranga as margens {nome1}.')
    print(f'De um povo heroico o brado {nome2}.')
    print(f'E o sol da liberdade em raios {nome3}.')
    print(f'Brilhou no céu da pátria nesse {nome4}.')

import time

time.sleep(5)
print('SEJA BEM VINDO AO PROCESSO DE SELEÇÃO')
time.sleep(5)
print('Antes de começarmos, precisamos  saber mais sobre você. Por favor, insira as seguintes informações: ')

print('Informe somente o seu primeiro  nome: ')
nome = str(input())

print('Informe a sua idade')
idade = int(input())

print('Informe a sua profissao')
prof = input()

print('Por que você quer entrar no Reality Show ?')
motivo = input()

print('O que você faria com 1,5 milhão de reais ? Escreva tudo !!! ')
salario = input()
print('  - - - Agradecemos pela inscrição - - - ')
time.sleep(5)
print('Vamos avaliar e analisar as suas respostas e em breve, entraremos em contato...')
time.sleep(5)
print('Estamos comparandos os seus dados com outros candidatos')

for i in 'Aguarde . . . . . . . . . . . . . . . . . . Status: Verificado ! \n':
    print(i, end='')
    time.sleep(0.25)

time.sleep(3)
print('PARABÉNS !!!! VOCÊ FOI SELECIONADO E SERÁ UNS DOS 5 PARTICIPANTES DO PROGRAMA :D ')
time.sleep(3)
print('Aqui estão algumas informações sobre os outros 2 participantes para que você não entre desatualizado ;) ')
time.sleep(5)

class Pessoa1:
    def __init__(self):
        self.nome = 'Felipe'
        self.idade = 29
        self.profissao = 'Professor'
        self.motivo = '"Sou inteligente e quero passar mais conhecimento."'
        self.dinheiro ='"Abrir uma escola no meu bairro."'

    def mostra_informacoes(self):
        print('Nome: ' + self.nome, ' / Idade: ' + str(self.idade) + ' anos', ' / Profissão: ' + self.profissao,' / Motivos: ' + self.motivo, ' / Com o prêmio: ' + self.dinheiro)

class Pessoa2:
    def __init__(self):
        self.nome = 'Paula'
        self.idade = 26
        self.profissao = 'Advogada'
        self.motivo = '"Sou destemina e julgo o que é certo e errado."'
        self.dinheiro = '"Investir na minha carreira."'

    def mostra_informacoes(self):
        print('Nome: '+self.nome, ' / Idade: '+str(self.idade) + ' anos', ' / Profissão: ' + self.profissao,' / Motivos: '+self.motivo,' / Com o prêmio: '+self.dinheiro)

class Pessoa3:
    def __init__(self):
        self.nome = 'João'
        self.idade = 38
        self.profissao = 'Engenheiro Mecânico'
        self.motivo = '"Gosto de brigar com as pessoas"'
        self.dinheiro = '"Viver viajando, se divertindo e gastar muito."'

    def mostra_informacoes(self):
        print('Nome: '+self.nome, ' / Idade: '+str(self.idade) + ' anos', ' / Profissão: ' + self.profissao,' / Motivos: '+self.motivo,' / Com o prêmio: '+self.dinheiro)

class Pessoa4:
    def __init__(self):
        self.nome = 'Marcela'
        self.idade = 30
        self.profissao = 'Médica'
        self.motivo = '"Quero provar a minha inteligência e estratégia."'
        self.dinheiro = '"Fazer um hospital e me tornar Diretora dele."'

    def mostra_informacoes(self):
        print('Nome: '+self.nome, ' / Idade: '+str(self.idade) + ' anos', ' / Profissão: ' + self.profissao,' / Motivos: '+self.motivo,' / Com o prêmio: '+self.dinheiro)

Alexandre = Pessoa1()
Paula = Pessoa2()
Joao = Pessoa3()
Marcela = Pessoa4()

lista = [Alexandre, Paula, Joao, Marcela]

for nome in lista:
    nome.mostra_informacoes()
    time.sleep(12)

print('Seus principais objetivos:')
time.sleep(3)
print(motivo)
time.sleep(3)
print(salario)

print('Muito bem. O jogo ira começar em: ')
time.sleep(2)
for i in range(10,-1,-1):
    time.sleep(1)
    print(i)

prova1()
















