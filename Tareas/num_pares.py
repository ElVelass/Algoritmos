A = list(map(int, input("Ingrese los numeros ").split()))
B = list(map(int, input("Ingrese los numeros ").split()))

set_A = set(A)
set_B = set(B)
pares_comunes = {x for x in set_A if x % 2 == 0}
pares_comunes.update(x for x in set_B if x % 2 == 0)

print(pares_comunes)