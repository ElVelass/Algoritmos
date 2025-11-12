a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))         # Unión: {1, 2, 3, 4, 5}
print(a.intersection(b))  # Intersección: {3}
print(a.difference(b))    # Elementos en a pero no en b: {1, 2}
print(a.symmetric_difference(b))  # Elementos distintos: {1, 2, 4, 5}

print(a.issubset(b))      # False, a no está contenido en b
print(a.issuperset({1}))  # True, a contiene al 1