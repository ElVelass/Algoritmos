tabla = int(input("Ingrese la tabla que desea practicar "))
cont = 1
numx = 0
punt = 0
while cont <= 10:
    print("Cuanto es: ", tabla, " x ", numx+1)
    rsta = int(input("Respuesta: "))
    cont += 1
    numx += 1
    if rsta == tabla*numx:
        punt += 1
        print("Felicidades")
    else:
        print("Respuesta correcta: ", tabla*numx)
if punt <= 5:
    print("Insuficiente")
elif punt <= 7:
    print("Aceptable")
elif punt <= 9:
    print("Sobresaliente")
else:
    print("Excelente")    