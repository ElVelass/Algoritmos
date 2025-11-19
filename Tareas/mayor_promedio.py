lista1 = int(input("Digite la lista de 5 digitos "))
lista2 = int(input("Digite la lista de 5 digitos "))
lista3 = int(input("Digite la lista de 5 digitos "))
lista4 = int(input("Digite la lista de 5 digitos "))
lista5 = int(input("Digite la lista de 5 digitos "))
lista = [lista1, lista2, lista3, lista4, lista5]
ya = []
prom = (lista1 + lista2 + lista3 + lista4 + lista5)/5
for x in lista:
    if x > prom:
        ya.append(x)
print("Mayores que el promedio: ", ya)
print("Promedio: ", prom)

