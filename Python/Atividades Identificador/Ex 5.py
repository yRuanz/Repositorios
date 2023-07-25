import os

# Infantil A - ATÉ 6 / Infantil B - 6 a 10 / Juvenil A - 10 A 15 / Juvenil B - 15 a 20 / Adulto - +20

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
x = int(input("Informe sua idade:"))

if x > 1 and x < 6:
    print("A categoria do nadador é Infantil A")

elif x > 6 and x < 11:
    print("A categoria do nadador é Infantil B")

else:
    if x > 11 and x < 16 :
        print("A categoria do nadador é Juvenil A")

if x > 16 and x < 20:
    print("A categoria do nadador é Juvenil B")

elif x > 20:
    print("A categoria do nadador é Adulto")

os.system("pause")
