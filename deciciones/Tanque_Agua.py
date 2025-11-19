agua = float(input("Cuantos litros tiene el tanque?"))
if agua < 250:
    print("Abrir llave")
elif agua >= 250 and agua <= 450:
    print("Mantener asi")
else:
    print("Cerrar llave")