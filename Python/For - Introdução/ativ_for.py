import os

numeros = []

for i in range(5):
    num = int(input("Insira um número:"))
    numeros.append(num)

    maior = numeros[0]
    menor = numeros[0]

    for num in numeros:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

os.system("cls")

print("O maior número é:", maior)
print("O menor número é:", menor)

os.system("pause")