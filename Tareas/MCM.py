def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mcd(a, b)

num1 = int(input("Ingrese el num 1 "))
num2 = int(input("Ingrese el num 2 "))
print(mcm(num1, num2))
print(mcd(num1, num2))    