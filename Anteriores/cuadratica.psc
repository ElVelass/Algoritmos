Algoritmo cuadratica
	Definir x, x2, val, resl1 Como Real
	Escribir "Dime 3 numeros para la expresion cuadratica"
	Leer x2, x, val
	resl1 = ( x ^ 2 - 4 * x2 * val)^1/2
	si resl1 < 0 Entonces
		Escribir "La ecuacion no tiene solucion"
	SiNo
		Escribir "La ecuacion tiene solucion"
	FinSi
	
FinAlgoritmo
