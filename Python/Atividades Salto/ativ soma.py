import os

numeros = []

for i in range(5):
    num = int(input("Insira o valor do salto:"))
    numeros.append(num)

soma = 0
for num in numeros:
    soma += num

os.system("cls")

print("A soma é = ", soma)

os.system("pause")

