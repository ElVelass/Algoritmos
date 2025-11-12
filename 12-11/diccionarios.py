persona = {"nombre": "Ana", "edad": 25, "ciudad": "Bogotá"}
print(persona["nombre"])      # Ana
print(persona.get("correo"))  # None (no existe esa clave)
print(f"Hola soy {persona["nombre"]} tengo {persona["edad"]} años y soy de {persona["ciudad"]}")

persona["correo"] = "ana@example.com"  # Agrega nueva clave
persona["edad"] = 26                   # Modifica edad existente
persona.update({"pais": "Colombia"})   # Agrega varias claves


valor = persona.pop("correo", None)    # Elimina clave y devuelve valor
ultimo = persona.popitem()             # Elimina y devuelve el último par

for clave in persona.keys():
    print("Clave:", clave)

for valor in persona.values():
    print("Valor:", valor)

for clave, valor in persona.items():
    print(clave, "→", valor)