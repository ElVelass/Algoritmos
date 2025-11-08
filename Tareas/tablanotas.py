nota = float(input("Digite su nota "))
if nota < 3:
    print("Insuficiente")
elif nota <= 3.5:
    print("Aceptable")
elif nota <= 4:
    print("Sobresaliente")
else:
    print("Excelente")