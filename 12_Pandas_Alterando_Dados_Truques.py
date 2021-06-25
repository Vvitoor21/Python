import pandas as pd

dados = pd.DataFrame(columns = ['Nome','Idade','Profissão','Motivo no programa','Após o Prêmio'])
dados

class Pessoa1:
    def __init__(self):
        self.nome = 'Felipe'
        self.idade = 29
        self.profissao = 'Professor'
        self.motivo = 'Passar mais conhecimento'
        self.dinheiro ='Abrir uma escola'
        
Alexandre = Pessoa1()

dados.loc[0,'Nome':'Após o Prêmio'] = Alexandre.nome,Alexandre.idade,Alexandre.profissao,Alexandre.motivo,Alexandre.dinheiro
dados

# Alterando nomes de colunas em um DataFrame com Pandas

mapa = { 
    "home" : "principal",
    "how_it_works" : "como_funciona",
    "contact" : "contato",
    "bought" : "comprou"
}
dados = dados.rename(columns = mapa)

pd.set_option('display.max_rows',1000) #mostra mais linhas
pd.set_option('display.max_columns',1000) #mostra mais colunas

dataset.dtypes # mostra os tipos de dados do dataframe

dataset.fillna(0, inplace = True)




