#Exemplificação dos Itens

class Programador:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta_trabalho = None 
        print(a + 1)
    #Se é definido uma variavel sem valor, ela só podera ser mudada por um modificador de acesso 
    
    def getFerramenta(self):
        return self.ferramenta_trabalho

    def setFerramenta(self, ferramenta):
        self.ferramenta_trabalho = ferramenta

class Computador:
    def __init__(self, marca, processador):
        self.marca = marca
        self.processador = processador

    def getMarca(self):
        return self.marca

    def getProcessador(self):
        return self.processador

class Celular:
    def __init__(self, marcaCel, modeloCel):
        self.marcaCel = marcaCel
        self.modeloCel = modeloCel  