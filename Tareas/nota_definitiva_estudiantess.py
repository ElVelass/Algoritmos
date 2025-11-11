numest = int(input("Ingrese el numero de estudiantes "))
cont = 0
aprov = 0
reprov = 0
prom = 0
while numest > cont:
    codigo = input("Ingrese el Codigo del estudiante ")
    nota = float(input("Ingrese Nota definitiva "))
    prom = nota + prom
    cont += 1
    if nota < 3.0:
        reprov += 1
    else:
        aprov += 1
prom = prom / numest
print("El promedio fue de ", prom)
print("Reprobaron ", reprov)
print("Aprobaron ", aprov)
