lista = input("Ingrese elementos separados por espacios: ").split()
tupla_sin_duplicados = tuple(set(lista))

print(tupla_sin_duplicados)