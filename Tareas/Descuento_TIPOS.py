print("Ingrese el tipo de su articulo")
print("1. Textil")
print("2. Electrodomestico")
print("3. Elemento de cocina")
print("4. Videojuego")
tipo = int(input())
precio = int(input("Digite el precio "))
if tipo == 1:
    print("El precio de su articulo es de ", precio)
elif tipo == 2:
    precio = precio - precio*0.037
    print("El precio de su articulo es de ", precio)
elif tipo == 3:
    precio = precio - precio*0.042
    print("El precio de su articulo es de ", precio)
elif tipo == 4:
    precio = precio - precio*0.078
    print("El precio de su articulo es de ", precio)