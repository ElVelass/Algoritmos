Algoritmo digitos_suma_yupi
	Definir num, digts, suma Como entero
	Escribir "Digite su numero"
	Leer num
	digts = 0
	suma = 0
	si num > 0 Entonces
		Mientras num >= 1 Hacer
			suma = suma + num MOD 10
			num = Trunc(num / 10) 
			digts = digts + 1
		FinMientras
		Escribir "Su numero tiene " digts " cifras"
		Escribir "La suma de los digitos es " suma
	SiNo
		Escribir "El numero es negativo"
	FinSi
	
FinAlgoritmo