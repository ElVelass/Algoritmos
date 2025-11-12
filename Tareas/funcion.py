valormax = int(input("Ingrese el valor maximo de x "))
x=0
for x in range(0, valormax+1, 2):
    funcion = x ** 3 + x ** 2 - 5
    print("Para x =", x, " F(x) = ", funcion)
