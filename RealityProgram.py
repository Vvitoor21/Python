import time
import random

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

class Usuario:
    def __init__(self):
        self.nome = input('Seu nome é ')
        self.idade = input('você tem: ')
        self.profissao = input('Você é:')
        self.motivo = input('Seu motivo: ')
        self.salario = input('Seu objetivo com o prêmio:')


Alexandre = Pessoa1()
Paula = Pessoa2()
Joao = Pessoa3()
Marcela = Pessoa4()
usuario = Usuario()

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

lista = [Alexandre, Paula, Joao, Marcela]

for nome in lista:
    nome.mostra_informacoes()
    time.sleep(12)

print('Seus principais objetivos:')
time.sleep(3)
print(usuario.motivo)
time.sleep(3)
print(usuario.salario)

print('Muito bem. O jogo ira começar em: ')
time.sleep(2)
for i in range(10,-1,-1):
    time.sleep(1)
    print(i)

tentativa = 5

def nome1():
    nome1 = 'plácidas'
    musica = ''
    global tentativa

    while musica != nome1:
        musica = input('Ouviram do ipiranga as margens: ')
        if musica != nome1:
            print('errado')
            tentativa = tentativa - 1
            print(f'Voce tem {tentativa} chances')
            if tentativa == 0:
                print('Chances acabaram')
                break
def nome2():
    nome2 = 'retumbante'
    musica = ''
    global tentativa

    while musica != nome2:
        musica = input('De um povo heroico o brado: ')
        if musica != nome2:
            print('errado')
            tentativa = tentativa - 1
            print(f'Voce tem {tentativa} chances')
            if tentativa == 0:
                print('Chances acabaram')
                break
def nome3():
    nome3 = 'fúlgidos'
    musica = ''
    global tentativa

    while musica != nome3:
        musica = input('E o sol da liberdade em raios: ')
        if musica != nome3:
            print('errado')
            tentativa = tentativa - 1
            print(f'Voce tem {tentativa} chances')
            if tentativa == 0:
                print('Chances acabaram')
                break
def nome4():
    nome4 = 'instante'
    musica = ''
    global tentativa

    while musica != nome4:
        musica = input('Brihou no céu da pátria nesse: ')
        if musica != nome4:
            print('errado')
            tentativa = tentativa - 1
            print(f'Voce tem {tentativa} chances')
            if tentativa == 0:
                print('Chances acabaram')
                break

nome1()

if tentativa > 0:
    nome2()
else:
    print('.')

if tentativa > 0:
    nome3()
else:
    print('.')

if tentativa > 0:
    nome4()
else:
    print('.')

print(f'Sua pontuação total:{tentativa} pontos')
lista =['Pamela','Michele','Marcos','Antonio',usuario.nome]

if tentativa != 0:
    time.sleep(3)
    print('VOCÊ NÃO FOI TÃO RUIM !!!!\n')
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

print(f'Participantes restantes: {lista}')
















