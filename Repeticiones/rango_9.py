num1 = int(input("Ingrese su numero 1 "))
num2 = int(input("Ingrese su numero 2 "))
cont = 0
for x in range(num1, num2+1):
    if cont < 1:
        if x % 9 == 0 and x != 0:
            print(f"Primer multiplo de 9 es {x}")
            cont += 1
            break
if cont == 0:
    print("No existe ninguno")
    