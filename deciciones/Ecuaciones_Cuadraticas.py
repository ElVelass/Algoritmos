
numa = int(input("Ingrese num a "))
numb = int(input("Ingrese num b "))
numc = int(input("Ingrese num c "))

if numa == 0:
    print("La ecuacion es lineal")
elif numa == 0 and numb == 0 and numc == 0:
    print("Tiene infinitas soluciones")
elif numa == 0 and numb == 0 and numc != 0:
    print("No tiene soluciones")

disc = (numb ** 2) - 4 * numa * numc

if disc < 0:
    print("No tiene raices reales")
else:   
    raiz1 = float(-numb + (disc ** (1/2)) / (2*numa))
    raiz2 = float(-numb - (disc ** (1/2)) / (2*numa))
    print("x1 = ", raiz1)
    print("x2 = ", raiz2)
    if raiz1 >= 0 and raiz2 >= 0:
        print("Ambas raices positivas")
    elif raiz1 < 0 and raiz2 < 0:
        print("Ambas raices negativas")
    else:
        print("Una raiz positiva y una negativa")
print("Discriminante = ", disc)
