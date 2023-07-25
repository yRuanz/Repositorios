import os
s = 0
competidores = 0
def Menu(x):
    if x == 1:
        Registrar()
        s = 0
    elif x == 2:
        Alterar()
        s = 0
    elif x == 3:
        Listar()
        s = 0
    elif x == 4:
        s = 1
    else:
        print("Opção Inválida")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
def Registrar():
    
    os.system("cls")
    nome = input("Digite o nome do competidor: ")
    val = []
    for num in range(t):
        num = float(input("Digite a distancia do salto: "))
        val.append(num)
        competidores[nome] = val #salva uma lista com os saltos dentro do nome do usuario
    os.system("cls")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
def Alterar():
    print("")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
def Listar():
     os.system("cls")
for nome, saltos in competidores.items():
            soma_saltos = 0
            qtd_saltos = 0
            for salto in saltos:
                    soma_saltos += salto
                    qtd_saltos += 1
            media = soma_saltos / qtd_saltos
            print(f"{nome}: {saltos}, Média: {media:.2f}")
            os.system("pause")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
while s == 0:
    print("Escolha o que deseja:\n 1- Registrar Equação \n4- Sair")
    op =int(input("Digite sua opção:"))
    s = Menu(op)
 
os.system("pause")