class Cachorro: 
    def __init__(self,nome,idade,raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def latir(self):
        print("*Auuuuuuuuuuuuuuu*")
    
    def andar(self):
        print("*Andando*")

    def andar_com_estilo(self):
        print("*Moonwalk*")

    def correr(self):
        print("*Zuuummm*")

dog = Cachorro("Rex", 2, "Pitbull")

dog2 = Cachorro("Chico",4,"Cachorro Caramelo")

dog.andar_com_estilo()
print(dog.raca)

dog2.andar()
print(dog2.nome)