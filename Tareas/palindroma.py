def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == invertir(cadena)
cadena = input("Ingrese la cadena ")
print(es_palindromo(cadena))