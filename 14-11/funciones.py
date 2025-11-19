def mostrar_mayor(a, b):
    """Muestra cuál de los dos números es mayor."""
    if a > b:
        print("El mayor es:", a)
    elif b > a:
        print("El mayor es:", b)
    else:
        print("Son iguales")

mostrar_mayor(10, 7)

def sumar(a, b):
    """Devuelve la suma de a y b."""
    resultado = a + b
    return resultado

x = 3
y = 5
s = sumar(x, y)  # Llamada a la función
print("La suma es:", s)

def saludar():
    """Imprime un saludo fijo."""
    print("Hola, bienvenido a Python")

saludar()

def saludar_persona(nombre, saludo="Hola"):
    """Muestra un saludo personalizado usando un saludo por defecto."""
    print(saludo, nombre)

saludar_persona("Ana")                # Usa el valor por defecto "Hola"
saludar_persona("Luis", "Buenas")     # Sobrescribe el valor por defecto

def dividir_y_resto(a, b):
    """Devuelve el cociente y el resto de dividir a entre b."""
    cociente = a // b
    resto = a % b
    return cociente, resto  # Devuelve una tupla

r, q = dividir_y_resto(10, 3)
print("Cociente:", q)
print("Resto:", r)


