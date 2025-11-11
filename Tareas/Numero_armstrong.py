num = int(input("Digite el numero "))
num2 = num
num3 = num
digit = 0
suma = 0
if num < 0:
    print("El numero es negativo")
else:
    while num >= 1: 
        num /= 10
        num = int(num)
        digit += 1
    while num3 >= 1:
        suma += (num3 % 10)**digit
        num3 /= 10
        num3 = int(num3)
if suma == num2:
    print("Es un numero de armstrong")
else:
    print("No es un numero de armstrong")
print("Cifras: ", digit)
