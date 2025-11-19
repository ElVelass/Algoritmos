num = int(input("Digite el numero "))
digit = 0
suma = 0
if num < 0:
    print("El numero es negativo")
else:
    while num >= 1:
        suma = num % 10 + suma
        num /= 10
        num = int(num)
        digit += 1
print("Cifras: ", digit)
print("La suma es: ", suma)