lista_a = list(map(int, input("Lista A: ").split()))
lista_b = list(map(int, input("Lista B: ").split()))

producto_escalar = sum(a * b for a, b in zip(lista_a, lista_b))

print(f"Producto escalar = {producto_escalar}")