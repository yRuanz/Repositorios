class Carro:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getAno(self):
        return self.ano

    def getAno(self, ano):
        self.ano = ano
        
# FIAT UNO 2017 | CHEVROLET CELTA  2012| VOLKSWAGEN GOL 2018 | FIAT PALIO 2009 | FORD ECO SPORT 2007 | VOLKSWAGEN FUSCA  1996

class Roda:
    def __init__(self, marca, aro):
        self.marca = marca
        self.aro = aro

    def getRoda(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getRoda(self):
        return self.aro

    def setRoda(self, aro):
        self.aro = aro

 #PIRELLI | MICHELLAN

class Motor:
    def __init__(self, modelo, potencia):
        self.modelo = modelo  
        self.potencia = potencia

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getPotencia(self):
        return self.potencia

    def setPotencia(self, potencia):
        self.potencia = potencia

# 1.6 FIAT | 2.0 CHEVROLET | PEUGEOT 1.2