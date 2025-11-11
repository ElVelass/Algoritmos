costo = int(input("Digite el costo de su articulo"))
if costo >= 150000:
    costofinal = costo + costo *0.05
    print("Su costo final es de ", costofinal)
else:
    print("Su costo final es de ", costo)