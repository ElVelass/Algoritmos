Algoritmo tanque_agua
	Definir litros	Como Entero
	Escribir "Diga litros"
	Leer litros
	si litros >= 250 y litros <= 450 Entonces
		Escribir "Debe cerrar la llave"
	SiNo
		si litros < 250 Entonces
			Escribir "Debe abrir la llave"
		FinSi
		si litros > 450 Entonces
			Escribir "Debe vaciar el tanque"
		FinSi
	FinSi
FinAlgoritmo