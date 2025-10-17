Algoritmo nums_mayor
	Definir num1, num2, num3, num4 Como Entero
	Escribir "Dame 4 Numeros"
	Leer num1, num2, num3, num4
	si  num1 > num2 y num1 > num3 y num1 > num4 Entonces
		Escribir "El mayor es " num1
	SiNo
		si  num2 > num1 y num2 > num3 y num2 > num4 Entonces
			Escribir "El mayor es " num2
		SiNo
			si num3 > num1 y num3 > num2 y num3 > num4 Entonces
				Escribir  "El mayor es " num3
			SiNo
				si num4 > num1 y num4 > num2 y num4 > num3 Entonces
					Escribir "El mayor es " num4
				SiNo
					Escribir "Son iguales"
					
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
