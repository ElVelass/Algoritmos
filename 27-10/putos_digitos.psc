Algoritmo putos_digitos
	Definir num, cont, digito1, digito2, num2, digito3, ayuda, ayuda2, digito4 Como entero
	Escribir "Digite su numero"
	Leer num
	cont = 0
	num2 = num
	Mientras num >= 1 Hacer
		Trunc(num = num / 10) 
		cont = cont + 1
	FinMientras
	Escribir "Su numero tiene " cont " cifras"
	digito1 = num2 % 10
	digito2 = num2 % 100 - digito1
	digito2 = digito2 / 10
	ayuda = num2 % 100
	ayuda2 = num2 % 1000
	digito3 = num2 % 1000 - ayuda
	digito3 = digito3 / 100
	digito4 = num2 % 10000 - ayuda2
	digito4 = digito4 / 1000
	si num2 < 10 Entonces
		Escribir "La suma de sus digitos es " digito1
	SiNo
		si num2 < 100 Entonces
			Escribir "La suma de sus digitos es " digito1 + digito2
		SiNo
			si num2 < 1000 Entonces
				Escribir "La suma de sus digitos es " digito1 + digito2 + digito3
			SiNo
				si num2 < 10000 Entonces
					Escribir "La suma de sus digitos es " digito1 + digito2 + digito3 + digito4
				FinSi
			FinSi
		FinSi
	FinSi


	
FinAlgoritmo
