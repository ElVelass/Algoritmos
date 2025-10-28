Algoritmo haga_num_impares
	Definir cont, num, res Como Entero
	Escribir "Digite la cantidad de digitos"
	Leer num
	res = 1
	cont = 0
	Repetir
		Escribir res
		cont = cont + 1
		res	= res + 2
	Hasta Que cont = num
FinAlgoritmo
