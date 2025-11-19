nota1 = float(input("Diga su nota 1: "))
nota2 = float(input("Diga su nota 2: "))
nota3 = float(input("Diga su nota 3: "))
nota4 = float(input("Diga su nota 4: "))
nota5 = float(input("Diga su nota 5: "))
notafinal = (nota1 + nota2 + nota3 + nota4 + nota5)/5
if notafinal >= 3.5:
    print("Paso con ", notafinal)
else:
    print("Perdio con ", notafinal) 