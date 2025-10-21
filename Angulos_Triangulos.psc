Algoritmo Angulos_Triangulos
	Definir angulo, equivalente, seno, coseno, rad Como Real
	Escribir "Digite su angulo"
	Leer angulo
	equivalente = angulo MOD 360
	si equivalente < 0 Entonces
		equivalente = equivalente + 360
	FinSi
	rad = equivalente * PI / 180
	seno = sen(rad)
	coseno = cos(rad)
	Escribir "cos = " coseno
	Escribir "sen = " seno
	Escribir "Angulo equivalente = " equivalente
	si equivalente > 0 y equivalente < 90 Entonces
		Escribir "Cuadrante I"
		Escribir "Tipo: Agudo"
		Escribir "Seno Positivo, Coseno Positivo"
	SiNo
		si equivalente > 90 y equivalente < 180 Entonces
			Escribir "Cuadrante II"
			Escribir "Tipo: Obtuso"
			Escribir "Seno Positivo, Coseno Negativo"
		SiNo
			si equivalente > 180 y equivalente < 270 Entonces
				Escribir "Cuadrante III"
				Escribir "Tipo: Concavo"
				Escribir "Seno Negativo, Coseno Negativo"
			SiNo
				si equivalente > 270 y equivalente < 360 Entonces
					Escribir "Cuadrante IV"
					Escribir "Tipo: Concavo"
					Escribir "Seno Negativo, Coseno Positivo"
				SiNo
					si equivalente = 90 Entonces
						Escribir "Sobre las lineas"
						Escribir "Tipo: Recto"
						Escribir "Seno Positivo, Coseno Positivo"
					SiNo
						si equivalente = 270 Entonces
							Escribir "Sobre las lineas"
							Escribir "Tipo: Recto"
							Escribir "Seno Negativo, Coseno Positivo"
						SiNo
							si equivalente = 180 Entonces
								Escribir "Sobre las lineas"
								Escribir "Tipo: Llano"
								Escribir "Seno Positivo, Coseno Negativo"
							FinSi
						FinSi
					FinSi
					
					FinSi
					
			FinSi
		FinSi
	FinSi
FinAlgoritmo
