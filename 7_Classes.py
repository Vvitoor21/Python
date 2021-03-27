class Pessoa:   #NOME, IDADE, CIDADE
    def __init__(self):
        self.nome = 'Vitor'
        self.idade = 22
        self.cidade = 'Sao Paulo'
    pass

vitor = Pessoa()
print(vitor.nome)
print(vitor.idade)
print(vitor.cidade)

print('---------------------------------------------------------------------------------------------------------------')

class Individuo:
    def __init__(self, nome, idade, cidade):
        self.nome = print(f'Seu nome é {nome}')
        self.idade = print(f'você tem {idade}')
        self.cidade = cidade
    pass

indi1 = Individuo('Eduardo',54,'Rio')
indi2 = Individuo('Pamela',29,'Para')

print('---------------------------------------------------------------------------------------------------------------')

class Pessoa:
    def falar(self):
        print("EU ESTOU FALANDO")
    def durmir(self):
        print("EU ESTOU DORMINDO")

P = Pessoa()
P.durmir()
P.falar()

print('----------------------------------------------------------------------------------------------------------------')

class acoes:
    def estudando(self):
        print('Estudando no momento. Por favor, não me atrapalhe. Obrigado :) ')
    def trabalhando(self):
        print('Trabalahndo no momento. Volte depois')
    def desocupado(self):
        print('Momento livre. Pode dizer o que deseja')
    def viajando(self):
        print('Impossível estabelecer comunicação devido a distancia')

humano = acoes()

print('DIGITE SEU STATUS')

resp=input()

while resp not in ('trabalhando','estudando','desocupado','viajando'):
    resp=input('Digite novamente')
if resp == 'trabalhando':
    humano.trabalhando()
elif resp == 'estudando':
     humano.estudando()
elif resp == 'desocupado':
     humano.desocupado()
elif resp == 'viajando':
    humano.viajando()
