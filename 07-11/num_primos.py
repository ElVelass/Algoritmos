num = int(input("De un numero "))
cont = 0
cont2 = 0
if num < 1:
    print("El numero no es primo")
while cont <= num:
    cont = cont + 1
    if num % cont == 0:
        cont2 = cont2 + 1
if cont2 == 2 or num == 1:
    print("El numero es primo")
else:
    print("El numero no es primo")
    
