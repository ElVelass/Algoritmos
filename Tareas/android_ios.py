cant = int(input("Cuantos estudiantes "))
cont = 0
ios = 0
andro = 0
while  cont < cant:
    cod = input("Digite su codigo ")
    print("Digite su voto")
    print("1. Android")
    print("2. iOS")
    print("3. Otros")
    voto = int(input(""))
    if voto == 1:
        andro += 1
    elif voto == 2:
        ios += 1
    cont +=1
print("Votos iOS: ", ios)
print("Votos Android: ", andro)

