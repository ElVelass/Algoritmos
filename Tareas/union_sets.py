B = set(list(map(int, input("Ingrese set 1: ").split())))
A = set(list(map(int, input("Ingrese set 2: ").split())))


union = A | B
diferencia = A - B

print(f"Unión: {union}")
print(f"Diferencia: {diferencia}")