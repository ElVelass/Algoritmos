num = int(input("Digite el numero "))
digit = 0
r = 0
if num < 0:
    print("El numero es negativo")
else:
    while num >= 1:
        r = r*10 + num % 10 
        num = num/10
        num = int(num)
        digit += 1
print("Cifras: ", digit)
print("El inverso es", r)