import os

print("1 - Número Primo")
print("2 - Número Decrescente")
print("3 - Mediana de três números")
print("4 - Sair")

numep = 1
numedec = 2
median = 3
sair = 4

op = int(input("Coloque a operação que deseja realizar:"))

#1 - - - - - - - - - - Número Primo - - - - - - - - - -1#
if (op == 1):
    print("Você escolheu Números Primos!")
    print("1 - Realizar cálculo")
    print("2 - Refazer")
    print("3 - Voltar")
        
    op = int(input("Escolha o que deseja fazer:"))
    n1 = int(input("Coloque o número que deseja verificar:"))

    sobra = n1 % 2 

    if sobra == 1:
        print("É primo")
    else:
        print("Não é primo")   

#2 - - - - - - - - - - Número Decrescente - - - - - - - - - - 2#
if (op == 2):
    numedec = int(input("Você escolheu Números Decrescente!"))
print("1 - Realizar cálculo")
print("2 - Refazer")
print("3 - Voltar")
print("4 - Sair")
n = int(input("Número para realizar a ordem decrescente:"))
print (n)

p="N"

while p != n:
    while n>=0:
        print(n)
        n = n-1

#3 - - - - - - - - - - Mediana de três números - - - - - - - - - -3#

if (op == 3):
    median = int(input("Você escolheu Mediana de três números"))
print("1 - Realizar cálculo")
print("2 - Refazer")
print("3 - Voltar")
op = int(input("Escolha o que deseja fazer:"))
if median == 1:
    n1 = float(input("Digite o primeiro número"))
    n2 = float(input("Digite o segundo número"))
    n3 = float(input("Digite o terceiro número"))
    mediana = 0
            
    if n1 > n2:
        if n2 > n3:
             mediana = n3
        elif n1 > n3:
            mediana = n3
        else:
            mediana = n1

    else:
        if n2 < n3:
            mediana = n2
        elif n1 < n3:
            mediana = n3 
        else:
            mediana = n1

os.system("pause")
    
