agenda = {}

while True:
    entrada = input("Ingrese 'nombre - teléfono' o 'fin' para terminar: ")
    if entrada.lower() == 'fin':
        break
    
    if ' - ' in entrada:
        nombre, telefono = entrada.split(' - ')
        agenda[nombre] = telefono

print(agenda)