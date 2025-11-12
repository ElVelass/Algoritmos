s = {1, 2, 2, 3, 10} #no ordenada, sin elementos repetidos, mutable
print(s)

s.add(4)         # Agrega 4
print(s)
s.update([6, 5]) # Agrega varios valores
print(s)
s.remove(2)      # Elimina el 2, lanza error si no existe
print(s)
s.discard(10)    # No lanza error si el valor no existe
print(s)