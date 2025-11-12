frutas = ["manzana", "banana", "naranja"]
print(frutas[0])

frutas.append("uva")
frutas.insert(2, "pera")

frutas.remove("banana")
ultimo = frutas.pop()
print("Elemento eliminado: ", ultimo)
del frutas[2]
print(frutas)