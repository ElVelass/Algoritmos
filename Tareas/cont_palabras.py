frase = input("Ingrese una frase: ")

contador = {}
palabras = frase.lower().split()

for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1

print(contador)