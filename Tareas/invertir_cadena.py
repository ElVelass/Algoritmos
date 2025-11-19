def invertir(cadena):
    if len(cadena) == 0:
        return ""
    return invertir(cadena[1:]) + cadena[0]
cadena = input("Escriba la cadena ")
print(invertir("cadena"))