def prova1():
    nome1 = 'plácidas'
    nome2 ='retumbante'
    nome3 ='fúlgidos'
    nome4 ='instante'

    musica =''

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
print('Aqui estão algumas informações sobre os outros participantes para que você não entre desatualizado ;) ')
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
















