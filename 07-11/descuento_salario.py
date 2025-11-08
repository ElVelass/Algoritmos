salario = int(input("Cuanto gana "))
salud = salario*0.04
pension = salario*0.04
salarioneto = salario - salud - pension
print("Salud = ", int(salud))
print("Pension = ", int(pension))
print("Salario neto = ", int(salarioneto))