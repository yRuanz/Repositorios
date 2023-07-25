    import os 

linha = 0
coluna = 0
lista = [3, 1, 4, 6, 2, 5]

matriz = {
'0','0','0','0',
'0','0','0','0',
'0','0','0','0',
'0','0','0','0',
}

print("Instruções e manipule a Matriz 4x4\n\nAdicione o valor 3 na posição (3,1).\nAdicione o valor 1 na posição (1,2).\nAdicione o valor 4 na posição (0,0).\nAdicione o valor 6 na posição (0,3).\nAdicione o valor 2 na posição (2,2).\nAdicione o valor 5 na posição (3,3).\n")

for lista in range(6) : 
    linha = int(input(f"Coloque o valor da linha:"))
    coluna = int(input(f"Coloque o valor da coluna:"))

matriz = [linha],[coluna]

print(valor)