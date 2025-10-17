Algoritmo premio_notas
	Definir nota Como Real
	Escribir "Dame tu nota"
	Leer nota
	Si nota < 3.0 Entonces
		Escribir "Insuficiente :c"
	sino 
		si nota <= 3.5 Entonces
			Escribir "Aceptable :/"
		SiNo
			si nota <= 4 Entonces
				Escribir "Sobresaliente :)"
			SiNo
				si nota <= 5 Entonces
					Escribir "Excelente :D"
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
