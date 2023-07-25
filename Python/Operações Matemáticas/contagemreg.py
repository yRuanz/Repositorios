import os

n = int(input("Coloque um número para a contagem regressiva:"))
print (n)

p="N"

while p != n:
    while n>=0:
        print(n)
        n = n-1
    
    while True:
        resposta = input("Deseja continuar? (s/n) ")
        if resposta == "s":
            break
        print("Continuando...")   

os.system("pause")

