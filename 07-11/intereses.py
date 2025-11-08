cant = int(input("Cuanto piensa invertir "))
porc = int(input("Digite el porcentaje de interes "))
tiempo = int(input("Cuanto tiempo "))
intereses = (cant*porc*tiempo)/360
dinerorecaudado = cant + intereses - intereses*0.07
print("El dinero total recaudado es de ", int(dinerorecaudado)) 