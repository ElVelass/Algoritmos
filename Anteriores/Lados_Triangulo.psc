Algoritmo Lados_Triangulo
	Definir a, b, c Como Entero
	Escribir  "Dime los 3 lados del triangulo"
	Leer a, b, c

	si No(a + b > c y a + c > b y b + c > a) Entonces
		Escribir "Forma un triangulo invalido"
	SiNo
			si (a + b > c y a + c > b y b + c > a) Entonces
				Escribir "Forma un triangulo valido"
				si a = b y a = c y b = c Entonces
					Escribir "Equilatero"
				SiNo
					si a = b o a = c o b = c Entonces
						Escribir "Isoseles"
					SiNo
						Escribir "Escaleno"
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
