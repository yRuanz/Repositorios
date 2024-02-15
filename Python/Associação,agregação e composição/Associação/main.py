from classes import *

funcionario = Programador("Carlos")
equipamento = Computador("Avell","Intel Core I5")
aparelho = Celular("Samsung", "S22 Ultra")

funcionario.setFerramenta(equipamento)
print(funcionario.ferramenta_trabalho.marca)
print(funcionario.ferramenta_trabalho.processador)
print("#########################################")
print(funcionario.getFerramenta().marca)
print("#########################################")
print(funcionario.getFerramenta().getMarca()) 
# É instanciado O tipo de objeto, o nome do programador(de onde a classe vem) e de onde o objeto vem 

