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
