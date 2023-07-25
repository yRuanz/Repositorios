
import os

t = 0 # váriavel que representa o número total
sobra = 0 # varíavel que representa a sobra dos cálculos
Na = 0 # váriavel do Número Atual

qtd = [] #lista dos números totais

t = int(input("Defina seu número:")) #define um número para a váriavel total

for num in range(t):
    Na = print(num+1) # exibe todos os números da lista 
qtd.append(Na) # computa o proximo número da lista

if sobra == num % 3: # condição para calcular se o Número atual é divisivel por 3
    sobra == 0 # condição para calcular se o Número atual é divisivel por 3 com base na sobra do calculo
    input("Jundiaí") # exibe a palavra jundiaí
elif sobra == num % 5: # condição para calcular se o Número atual é divisivel por 5
    sobra == 0
    input("Senai")
elif sobra == num % 5 and num % 3: # condição para calcular se o Número atual é divisivel por 3 e por 5
    sobra == 0
    input("SenaiJundiai")
else:    
    print(Na)

os.system("pause")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#corrigido

n= int(input("Digite um número inteiro positivo: "))

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("SenaiJundiai")
    elif i % 3 == 0:
        print("Senai")
    elif i % 5 == 0:
        print("Jundiai")
    else:
        print(i)

os.system("pause")