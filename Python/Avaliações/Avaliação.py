#CPF = 478 097 988 98
#Senha = 297 347

# 01
import os

input("Digite seu CPF:")
input("Digite sua Senha:")

C = int(478)
P = int(297)
F = int(988)
x = int(297347)

# 02
if C == 478 and P == 297 and F == 988: 
    print("CPF correto")
else:
    print("CPF incorreto")

if x == 297347:
    print("Senha correta")
else:
    print("Senha incorreta")

if C == 478 and P == 297 and F == 988 and x == 297347 == False:
    print("CPF e Senha incorreta")

os.system("pause")
