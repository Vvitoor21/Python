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

distribuicao_freq_quantitativa = pd.DataFrame({'Frequencia':frequencia_01, 'Porcentual':porcentual_01})
distribuicao_freq_quantitativa.rename_axis('Rendas', axis = 'columns', inplace = True)
distribuicao_freq_quantitativa.reset_index() # Restaurando index de um DataFrame
dataset.mean() # Pegar a media de todas as colunas

datase.groupby(['Sexo']).mean() # Selecionando médias de colunas com agrupamentos

dataset.Coluna.median() # Calcula a Mediana 

dataset.mode() # Calcula o valor mais frequente Moda

for index, row in dataframe.iterrows():
    if dataframe['Sexo'] = 'f':
        dataframe['Sexo'] = 1:
            else dataframe['Sexo'] = 0
         
dfsexo = {'M':1,'F':0}

dataframe['Sexo'] = dataframe['Sexo'].map(dfsexo)

dataframe.to_csv('C:\user\vitor...') # salvando dataframe em formato csv
            
        
dados.rename(column = {})
dados.rename(index = {})
dados.columns.name =
dados.reset_index()
crosstab(dados.Coluna1, dados.Coluna2)
crosstab(dados.Coluna1, dados.Coluna2, aggfunc = 'mean', values = dados.Coluna3)
dados.map()
dados['Coluna'].value_counts()
dados.shape
dados.rename_axis('Titulo', axis = 'columns')
dados.mean()
dados.mode()
dados.median()
dados.describe()
dados.mean()

