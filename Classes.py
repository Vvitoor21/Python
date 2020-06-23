class Computador:
    def __init__(self,marca,memoria_ram,placa_de_video):#__init_ serve para inicializarmos o objeto.
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video= placa_de_video
    def Ligar(self):
        print('Estou Ligando')

    def Desligar(self):
        print('Estou Desligando')

    def ExibirInformações(self):
        print(self.marca,self.memoria_ram,self.placa_de_video)

Computador1 = Computador('Windows','8GB','VGA')

Computador1.ExibirInformações()

class Carro:
    def __init__ (self,marca,cor,velocidade):
        self.marca= marca
        self.cor = cor
        self.velocidade = velocidade
    
    def Zero(self):
        print("Carro zero km")
    
    def Lugares(self):
        print('Compartimento para 5 pessoas e um porta-malas')
    
    def PropriedadesCarro(self):
        print(self.marca,self.cor,self.velocidade)

Carro1 = Carro('Ferrari','vermelho','280km')
Carro1.PropriedadesCarro()
Carro1.Lugares()
