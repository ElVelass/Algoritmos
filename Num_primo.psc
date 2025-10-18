Algoritmo Num_primo
	Definir num, contador, div Como Entero
	Escribir "Dime un numero entre 1 y 20"
	Leer num
	si num <= 1 Entonces
		Escribir "No es primo"
	SiNo
		Para div = 1 Hasta num Hacer
			si num MOD div = 0 Entonces
				contador = contador + 1
				
			FinSi
		FinPara
		si contador = 2 Entonces
			Escribir "Es primo"
		SiNo
			Escribir "No es primo"
		FinSi
	FinSi
	
FinAlgoritmo
