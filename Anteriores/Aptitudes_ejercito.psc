Algoritmo Aptitudes_ejercito
	Definir genero como cadena
	Definir estado, edad Como Entero
	Definir altura Como Real
	Escribir "Escriba su genero (todo en minusculas)"
	Leer genero
	Escribir "Escriba en metros su altura"
	Leer altura
	Escribir "Escriba su edad"
	Leer edad
	Escribir "Elija una de las 2 opciones"
	Escribir "Estado civil"
	Escribir "1. Soltero"
	Escribir "2. Casado"
	Leer estado	
	si (genero = "mujer" o genero = "femenino") y (estado =1) y (edad >= 20 y edad <= 25) y (altura >1.60) Entonces
		Escribir "Es apta para la ejercito"
	SiNo
		si (genero = "hombre" o genero = "masculino") y (estado =1) y (edad >= 18 y edad <= 24) y (altura >1.65) Entonces
			Escribir "Es apto para el ejercito"
		SiNo
			Escribir "No es apt@ para el ejercito"
		FinSi
	FinSi

FinAlgoritmo
