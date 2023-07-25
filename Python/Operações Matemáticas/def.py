import os

def soma(a,b):
    s = a + b
    if s > 0:
        v = True
    else:
        v = False
    return v

a = int(input("Informe o valor:"))
b = int(input("Informe o valor:"))

print(soma(a,b))
os.system("pause")
