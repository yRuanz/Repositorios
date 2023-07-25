import os

nome1 = input("informe seu nome:")
idade1 = int(input(f"Informe sua idade {nome1}: "))

nome2 = input("informe seu nome:")
idade2 = int(input(f"Informe sua idade {nome2}: "))

print(f"O aluno {nome1} tem {idade1} enquanto o {nome2} tem {idade2}")

idadet = idade1 + idade2 or idade2 + idade1

if idade1 > idade2 : 
 print(f"O aluno {nome1} é mais velho pois tem {idade1} e o {nome2} {idade2} anos de idade ")

else:
    print(f"O aluno {nome2} é mais velho pois tem {idade2} e o {nome1} {idade1} anos de idade ")
    print(f"a soma das idades é {idadet}")


   
os.system("pause")

