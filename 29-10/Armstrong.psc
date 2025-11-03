Algoritmo Armstrong
	Definir num, digts, numarm, cont, num2, num3 Como entero
	Escribir "Digite su numero"
	Leer num
	cont = 0
	numarm = 0
	num2 = num
	num3 = num
	si num < 0 Entonces
		Escribir "El numero es negativo"
	SiNo
		Mientras num >= 1 Hacer
		cont = cont + 1
		num = Trunc(num / 10) 
	FinMientras
	Mientras num2 >= 1 Hacer
		numarm = numarm + (num2 MOD 10) ^ cont
		num2 = Trunc(num2 / 10) 
	FinMientras
	si num3 = numarm Entonces
		Escribir "Es un numero de Armstrong"
	SiNo
		Escribir "No es un numero de Armstrong"
	FinSi
FinSi

FinAlgoritmo