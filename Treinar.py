print("PARTICIPANTES")
print( '- - - ATENÇÃO PARA ALGUNS COMANDOS DURANTE O PROCESSO - - - !!!')
print('1° >  Digite o nome do participante + ".mostra_informacoes " para saber um!!')

class Pessoa:
    def __init__(self):
        self.nome = 'Vitor'
        self.idade = 22
        self.profissao = 'Programador'

    def mostra_informacoes(self):
        print(self.nome, self.idade, self.profissao)

    def __repr__(self):
        return str(self.__dict__)

class Pessoa2:
    def __init__(self):
        self.nome = 'Amanda'
        self.idade = 29
        self.profissao = 'Engenheiro'

    def mostra_informacoes(self):
        print(self.nome, self.idade, self.profissao)

    def __repr__(self):
        return str(self.__dict__)

vitor = Pessoa()
amanda = Pessoa2()

vitor.mostra_informacoes()

print('LISTA DE PARTICIPANTES : ')
lista = [ vitor.nome, amanda.nome, ]

print(lista)

input()
