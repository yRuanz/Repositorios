import os

print("[ Tabela de Preços][Preços]")
print("[-------------------------]")
print("[ Manga           ][  10  ]")
print("[ Pera            ][  20  ]")
print("[ Abacaxi         ][  30  ]")
print("[ Morango         ][  40  ]")
print("[ Banana          ][  50  ]")
print("--------------------------")

x = int(input("Escolha um produto:"))

if (x == 1):
    print("O valor do produto é R$10")

if (x == 2):
    print("O valor do produto é R$20")

if (x == 3):
    print("O valor do produto é R$30")
    
if (x == 4):
    print("O valor do produto é R$40")

if (x == 5):
    print("O valor do produto é R$50")

if (x > 5):
    print("O Produto escolhido não esta à venda")

os.system("pause")
