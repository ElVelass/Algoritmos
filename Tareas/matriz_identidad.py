num = int(input("Digite el numero de la matriz "))
matriz = []
for i in range(num):
    fila = []
    for x in range(num):
        if i == x:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)
print(f"La matriz {num} x {num}")
for fila in matriz:
    print(fila)