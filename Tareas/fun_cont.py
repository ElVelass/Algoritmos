def contar_digitos(n):
    if n == 0:
        return 1
    
    # Manejar números negativos
    if n < 0:
        n = -n
    
    contador = 0
    while n > 0:
        contador += 1
        n = n // 10
    return contador
num = int(input("Ingrese su numero "))
print(contar_digitos(num), "Digitos")
  