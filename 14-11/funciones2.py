x = 10  # Variable global

def ejemplo():
    y = 5  # Variable local
    print("Dentro de la función, x =", x)
    print("Dentro de la función, y =", y)

ejemplo()
print("Fuera de la función, x =", x)
# La siguiente línea daría error si se descomenta:
#print("Fuera de la función, y =", y)  # y no existe fuera de la función