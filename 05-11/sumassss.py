suma = 0
while True:
    x = int(input("Ingrese el numero "))
    if x < 0:
        continue
    elif x == 0:
        print("Suma total: ", suma)
        break
    suma = x + suma
    print(suma)
