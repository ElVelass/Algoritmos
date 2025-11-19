while True:
    print("Elija una de las siguientes opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Finalizar")
    elije = int(input(""))
    if elije == 1:
        num1 = int(input("Numero 1 "))
        num2 = int(input("Numero 2 "))
        print("La suma es: ", num1 + num2)
    elif elije == 2:
        num1 = int(input("Numero 1 "))
        num2 = int(input("Numero 2 "))
        print("La resta es: ", num1 - num2)
    elif elije == 3:
        break
    else:
        continue