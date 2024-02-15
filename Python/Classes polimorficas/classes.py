# class Veiculo():

#     def mover(self):
#         print("")

#     pass
# class Carro():

#     def mover(self):
#         print("anda com as 4 rodas no chão")

# class Moto():

#     def mover(self):
#         print("anda com as 2 rodas no chão")

from abc import *



class Poligono(ABC):
    @abstractclassmethod
    def __init__(self):
        self.lado = None

    def qtd_lados(self):
        return self.lado

class Quadrado(Poligono):
    def __init__(self):
        self.lado = 4

class Triângulo(Poligono):
    def __init__(self):
        self.lado = 3