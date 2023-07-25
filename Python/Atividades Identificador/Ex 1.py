import os

y = 1
n = 1
s = y+1

while y == n:

    x = int(input("Informe o número:"))

    if x < 0:
        print(f"O número {x} é negativo")
    else :
        print(f"O número {x} é positivo")

    if x == 0:
        print(f"O número {x} é igual a zero")
    
    input("Você deseja sair?\nSim = s \nNão = n\n")

while s == y+1:


    os.system("pause")