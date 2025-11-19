def potencia(base, exponente):
    if exponente == 0:
        return 1
    if exponente < 0:
        return 1 / potencia(base, -exponente)
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado
base = int(input("Ingrese la base "))
potencia = int(input("Ingrese la potencia "))
print(potencia(base, potencia))