costo = input("Digite el costo de su articulo ")
costo = int(costo)
if costo >= 150000:
    costofinal =  costo - costo * 0.05
    print("Precio articulo = ", costofinal)
else: 
        print("Precio articulo = ", costo)