ran1 = int(input("Primer rango"))
ran2 = int(input("Primer rango"))
ran3 = int(input("Segundo rango"))
ran4 = int(input("Segundo rango"))
ran5 = int(input("Tercer rango"))
ran6 = int(input("Tercer rango"))
num = int(input("Numero para el rango"))
if num > ran1 and num < ran2 or num > ran3 and num < ran4 or num > ran5 and num < ran6:
    print("Se encuentra dentro del rango")
else:
    print("No se encuentra dentro del rango")