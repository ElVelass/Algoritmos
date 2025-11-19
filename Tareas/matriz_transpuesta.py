matriz = [[1,2,3],[4,5,6]]
mtran1 = []
mtran2 = []
mtran3 = []
mtran = []
cont = 0
for fila in matriz:
    for columna in fila:
        cont+=1
        if cont == 1 or cont == 4:
            mtran1.append(columna)
        elif cont == 2 or cont == 5:
            mtran2.append(columna)
        elif cont == 3 or cont == 6:
            mtran3.append(columna)
mtran.append(mtran1)
mtran.append(mtran2)
mtran.append(mtran3)
print(mtran)