Algoritmo sin_titulo
	Definir nota, notas, cant, cont, cod, perd, pasa Como Real
	Escribir "Digite la cantidad de estudiantes"
	Leer cant
	cont = 0
	notas = 0
	perd = 0
	pasa = 0
	Mientras cont < cant
		Escribir "Digite codigo del estudiante y su nota"
		Leer cod, nota
		si nota < 3.0 Entonces
			Escribir "El estudiante " cod " perdio la materia"
			perd = perd + 1
		SiNo
			Escribir "El estudiante " cod " paso la materia"
			pasa = pasa + 1
		FinSi
		cont = cont + 1
		notas = nota + notas
	FinMientras
	notas = notas / cant
	Escribir "El promedio total de todos los estudiantes es de " notas
	Escribir "Pasaron " pasa " estudiantes"
	Escribir "Perdieron " perd " estudiantes"
	
FinAlgoritmo
