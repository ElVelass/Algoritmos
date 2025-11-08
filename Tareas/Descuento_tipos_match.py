tipo = int(input("Digite su tipo de descuento"))
costo = int(input("Digite el costo de su articulo"))
match tipo:
    case 1:
        print("Su costo final es de ", costo - costo * 0.125)
    case 2:
        print("Su costo final es de ", costo - costo * 0.083)
    case 3:
        print("Su costo final es de ", costo - costo * 0.032)
    case _:
        print("Su costo final es de ", costo)