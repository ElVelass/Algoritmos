tupla1 = tuple(list(map(int, input("Ingrese la tupla 1 ").split())))
tupla2 = tuple(list(map(int, input("Ingrese la tupla 2 ").split())))
if tupla1 > tupla2:
    print("La primera tupla es mayor")
elif tupla1 < tupla2:
    print("La segunda tupla es mayor")
else:
    print("Las tuplas son iguales")