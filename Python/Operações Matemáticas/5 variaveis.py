import os

a = int(input("Informe o valor: "))
b = int(input("Informe o valor: "))
c = int(input("Informe o valor: "))
d = int(input("Informe o valor: "))
e = int(input("Informe o valor: "))

import statistics

list = [a,b,c,d,e]

print("A mediana é:")
print(statistics.median(list))

os.system("pause")
