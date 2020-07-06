class Pessoa:
    def __init__(self,nome,sobrenome,idade,altura,email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.altura = altura
        self.idade = idade
        self.email = email

    def ExibirInformaoes(self):
        print(f'Nome:{self.nome},Sobrenome:{self.sobrenome},Idade:{self.idade},Altura:{self.altura},Email:{self.email}.')

    def Permisao(self):
        if self.idade >= 18:
            print(f'{self.nome} tem {self.idade} anos.Autorização Confirmada...')
        else:
            print(f'{self.nome} tem {self.idade} anos.Acesso Negado...')


Pessoa1 = Pessoa('Vitor','Duarte',21,1.80,'vitor.bem@hotmail.com')
Pessoa2 = Pessoa('Eduardo','Souza',35,1.88,'edu.soso10@hotmail.com.br')
Pessoa3 = Pessoa('Amanda','Pereira',10,1.70,'amanda.pere2@hotmail.com')

Pessoa1.ExibirInformaoes()
Pessoa2.ExibirInformaoes()
Pessoa3.ExibirInformaoes()

print("...............................................................................................................")

Pessoa1.Permisao()
Pessoa2.Permisao()
Pessoa3.Permisao()

print("...............................................................................................................")

class Filme:
    def __init__(self,titulo,genero,faixa_etaria,duracao):
        self.titulo = titulo
        self.genero = genero
        self.faixa_etaria = faixa_etaria
        self.duracao = duracao

    def ExibiInfos(self):
        print(self.titulo,self.genero,self.faixa_etaria,self.duracao)

filme1 = Filme('Os Vingadores','Aventura','12 anos','3h e 10min')

filme1.ExibiInfos()
