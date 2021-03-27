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
"""
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
    
"""

print('----------------------------------------------------------------------------------------------------------------')

class Filme:
    def __init__(self,titulo,genero,faixa_etaria,duracao):
        self.titulo = titulo
        self.genero = genero
        self.faixa_etaria = faixa_etaria
        self.duracao = duracao

    def ExibiInfos(self):
        print(f'O nome do filme é : {self.titulo}')
    def duracao_e_idade(self):
        print(f'O filme tem duracao de {self.duracao} para faixa etária de {self.faixa_etaria} anos')


filme1 = Filme('Os Vingadores','Aventura','12','3h e 10min')

filme1.ExibiInfos()
filme1.duracao_e_idade()

