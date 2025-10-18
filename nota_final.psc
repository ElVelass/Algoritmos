Algoritmo nota_final
	Definir nota1, nota2, nota3, nota4, nota5, notafinal Como Real
	Escribir "Dime las notas de los 5 trabajos"
	Leer nota1, nota2, nota3, nota4, nota5
	notafinal = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
	si notafinal < 3.5 Entonces
		Escribir "Perdiste la materia con " notafinal
	SiNo
		Escribir "Pasaste la materia con " notafinal
	FinSi
FinAlgoritmo
