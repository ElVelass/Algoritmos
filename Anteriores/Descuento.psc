Algoritmo Descuento
	Definir tipo, precio Como Real
	Escribir "Precio de su articulo"
	Leer precio
	Escribir "Tipo de descuento"
	Leer tipo
	Segun tipo Hacer
			caso 1:
				Escribir "Su precio final es de: " precio - precio * 0.125
			Caso 2:
				Escribir "Su precio final es de: " precio - precio * 0.083
			Caso 3:
				Escribir "Su precio final es de: " precio - precio * 0.032
			De Otro Modo:
				Escribir "Su precio final es de: " precio
	FinSegun
FinAlgoritmo
