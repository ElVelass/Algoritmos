Algoritmo descuentos_tipos
	Definir tipo, costo Como real
	Escribir "Dime el tipo de tu producto"
	Escribir "1. Textil"
	Escribir "2. Electrodomestico"
	Escribir "3. Elemento de Cocina"
	Escribir "4. Videojuego"
	Leer tipo
	Escribir "Dime el costo del producto"
	Leer costo
	Segun tipo
		Caso 2:
			Escribir "El costo del producto queda en: " costo - costo * 0.037
		Caso 3:
			Escribir "El costo del producto queda en: " costo - costo * 0.042
		Caso 4:
			Escribir "El costo del producto queda en: " costo - costo * 0.078
		De Otro Modo:
			Escribir "El costo del producto queda en: " costo
	FinSegun
FinAlgoritmo
