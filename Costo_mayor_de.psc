Algoritmo Costo_mayor_de
	Definir costo Como real
	Escribir "Digite el costo de su articulo"
	leer costo
	si costo >= 150000 Entonces
		Escribir "El precio de su articulo queda en " costo - costo*0.05
	SiNo
		Escribir "El precio de su articulo se mantiene en " costo
		
	FinSi
FinAlgoritmo
