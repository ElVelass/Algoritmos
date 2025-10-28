Algoritmo Repetir_Android_Ios
	Definir cont, num, ios, android, codest, cant Como Entero
	Escribir "Digite la cantidad de votos"
	Leer cant
	cont = 0
	ios = 0
	android = 0
	Repetir
		cont = cont + 1
		Escribir "Digite su codigo de estudiante"
		Leer codest
		Escribir "Decida por que plataforma votar"
		Escribir "1. iOS"
		Escribir "2. Android"
		Escribir "3. Otro"
		Leer num
		si num = 1 Entonces
			ios = ios + 1
		SiNo
			si num = 2 Entonces
				android = android + 1
			FinSi
		FinSi
	Hasta Que cont = cant
	si ios > android Entonces
		Escribir "Ganador iOS"
	SiNo
		si android > ios Entonces
			Escribir "Ganador Android"
		SiNo
			Escribir "Empate"
		FinSi
	FinSi
	Escribir "Android: " android
	Escribir "iOS: " ios
FinAlgoritmo