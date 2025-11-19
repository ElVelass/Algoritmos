import math
angulo = int(input("Digite su angulo "))
angulonorm = angulo % 360
if angulonorm < 0:
    angulonorm = angulonorm + 360
rad = angulonorm * math.pi / 180
sen = math.sin(rad)
cos = math.cos(rad)
print("Angulo equivalente: ", angulonorm)
print("cos: ", cos)
print("sen: ", sen)
if angulonorm < 90 and angulonorm > 0:
    print("Cuadrante I")
    print("Tipo: Agudo")
    print("Seno Positivo, Coseno Positivo")
elif angulonorm > 90 and angulonorm < 180:
    print("Cuadrante II")
    print("Tipo: Obtuso")
    print("Seno Positivo, Coseno Negativo")
elif angulonorm > 180 and angulonorm < 270:
    print("Cuadrante III")
    print("Tipo: Concavo")
    print("Seno Negativo, Coseno Negativo")
elif angulonorm > 270 and angulonorm < 360:
    print("Cuadrante IV")
    print("Tipo: Concavo")
    print("Seno Negativo, Coseno Positivo")
elif angulonorm == 90:
    print("Cuadrante Lineas")
    print("Tipo: Recto")
    print("Seno Positivo, Coseno Positivo")
elif angulonorm == 180:
    print("Cuadrante Lineas")
    print("Tipo: Llano")
    print("Seno Positivo, Coseno Negativo")