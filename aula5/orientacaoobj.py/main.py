class Caneta:
    def __init__(self):
        self.cor = 'azul'
        self.ponta = 0.7
        self.tamanho =  13.0
        self.substrato = 'plastico'

    def escrever(self):
        pass    

print('==================================================')

caneta = Caneta()
print(caneta.ponta)   
class Pessoa:
    def __init__(self, idade):
        self.idade = idade    

    def verificar_idade(self):
        if self.idade <= 14:
            print('Criança')
        elif self.idade >=15 and self.idade <= 17:
            print('adolescente')
        elif self.idade >= 18 and self.idade <= 34:
            print('jovem')
        elif self.idade >= 35 and self.idade <=60:
            print('Adulto')
        else:
            print('idoso')        

pessoa =  Pessoa(17)
pessoa.verificar_idade()