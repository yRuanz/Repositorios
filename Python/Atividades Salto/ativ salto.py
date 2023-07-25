import os 

y = "N"
competidores = {}

while y != "S":
    print("[1] Registrar\n[2] Alterar\n[3] Listar\n[4] Sair")
    regist = 1
    alt = 2
    lista = 3
    sair = 4

    op = int(input("Selecione o que deseja realizar:"))

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    if op == 1:

        os.system("cls")
        print("Você selecionou registrar!")
        val = []
        t = 5
        nome =input("Digite o nome do atleta:")
        for num in range(t):
            salto = int(input(f"Insira o valor do {num+1}º salto de {nome}:"))
            val.append(salto)
            print("Salto registrado!")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    if op == 2:
        
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

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
    
    if op == 3:

        os.system("cls")
        print("Você selecionou listar!")
        
        for nome, saltos in competidores.items():
            soma_saltos = 0
            qtd_saltos = 0
            for salto in saltos:
                soma_saltos += salto
                qtd_saltos += 1
            media = soma_saltos / qtd_saltos
            print(f"{nome}: {saltos}, Média: {media}")
        os.system("pause")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    if op == 4:
        y = "S"

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#           
    
os.system("pause")