import os

competidores = 0
nome = 0
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
def Registrar(competidores):
    
    os.system("cls")
    print("Você selecionou registrar!")
    val = []
    t = 5
    nome =input("Digite o nome do atleta:")
    for num in range(t):
        salto = int(input(f"Insira o valor do {num+1}º salto de {nome}:"))
        val.append(salto)
        print("Salto registrado!")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
def Alterar(competidores):
    
    os.system("cls")
    print("Você selecionou alterar!")
    
    if nome in competidores:
        input("Insira o nome do atleta que deseja alterar:")

        print(f"Digite qual dos {t} valores da lista deseja alterar")
        p = int(input(""))
        competidores[nome][p] = float(input("Digite qual o novo valor do salto: "))
        os.system("pause")
    else:
        print("Competidor não encontrado")
    os.system("pause")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
def Listar(competidores):
    os.system("cls")
    print("Você selecionou listar!")

    if not competidores:
        print("Nenhum usuário cadastrado")
    else:
        for nome, saltos in competidores.items():
            soma_saltos = 0
            qtd_saltos = 0
            for salto in saltos:
                soma_saltos += salto
                qtd_saltos += 1
            media = soma_saltos / qtd_saltos
            print(f"{nome}: {saltos}, Média: {media}")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
w = "N"
while w != "S":
    os.system("cls")
    print("Selecione uma opção dentre as seguintes \n[1] Registro \n[2] Alterar \n[3] Listar \n[4] Sair")
    op = int(input("Digite a opção que deseja: "))

    if op == 1:
        os.system("cls")
        Registrar(competidores)
        os.system("cls")

    elif op == 2:
        os.system("cls")
        Alterar(competidores)
        os.system("cls")

    elif op == 3:
        os.system("cls")
        Listar(competidores)
        os.system("pause")

    elif op == 4:
        w = "S"
    else:
        print("Esta opção não está na lista")
