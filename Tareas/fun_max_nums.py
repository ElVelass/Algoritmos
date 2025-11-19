def maximo_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
num1 = int(input("Ingrese su numero 1 "))
num2 = int(input("Ingrese su numero 2 "))
num3 = int(input("Ingrese su numero 3 "))
print(maximo_de_tres(num1, num2, num3))