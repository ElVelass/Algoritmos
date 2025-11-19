coordenada = list(map(int, input("Ingrese las 2 coordenadas ").split()))
print(coordenada)
rango_min = int(input("Rango minimo "))
rango_max = int(input("Rango maximo "))
x, y = coordenada
if rango_min <= x <= rango_max and rango_min <= y <= rango_max:
    print("Dentro del rango")
else:
    print("Fuera del rango")