def aumentar(n):
    print(n)
    n += 10
    print(n)
x = 5
aumentar(x)

def actualizar_info(info):
    print(info)
    persona["edad"] += 1
    persona["Pais"] = "Colombia"
    print(info)
    return persona
persona = {"nombre": "Ana", "edad": 20}
actualizar_info(persona)
