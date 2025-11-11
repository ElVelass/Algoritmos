genero = input("Escriba su genero (todo en minusculas)")
altura = int(input("Escriba en metros su altura"))
edad = int(input("Escriba su edad"))
print("Elija una de las 2 opciones")
print("Estado civil")
print("1. Soltero")
print("2. Casado")
estado = input("")	
if genero == "mujer" or genero == "femenino" and estado == 1 and edad >= 20 and edad <= 25 and altura > 1.60:
    print("Es apta para la ejercito")
elif genero == "hombre" or genero == "masculino" and estado == 1 and edad >= 18 and edad <= 24 and altura > 1.65:
    print("Es apto para el ejercito")
else:
    print("No es apt@ para el ejercito")