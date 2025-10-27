Algoritmo intervalos3
	Definir num, inter1, inter2, inter3, inter4, inter5, inter6 Como Entero
	Escribir "Dime 2 numeros para el primer intervalo"
	Leer inter1, inter2
	Escribir "Dime 2 numeros para el segundo intervalo"
	Leer inter3, inter4
	Escribir "Dime 2 numeros para el tercer intervalo"
	Leer inter5, inter6
	Escribir "Dime un numero"
	Leer num
	si (num > inter1 y num < inter2) o (num > inter3 y num < inter4) o (num > inter5 y num < inter6) Entonces
		Escribir "El numero se encuentra dentro del intervalo"
	SiNo
		Escribir "El numero no se encuentra dentro del intervalo"
	FinSi
FinAlgoritmo
