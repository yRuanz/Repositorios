import os

a = int(input("Informe o valor de um lado: "))
b = int(input("Informe o valor de um lado: "))
c = int(input("Informe o valor de um lado: "))

if a == b and b == c and a == c:
    print("Esse mano é equilatero")

elif (a == b or (b != c or a != c)) or 8 == c or a == c:
    print("Esse mano é isoceles")

else:
    print("Esse mano é escaleno")
