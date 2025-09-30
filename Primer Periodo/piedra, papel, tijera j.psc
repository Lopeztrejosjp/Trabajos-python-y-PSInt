Algoritmo piedra_papel_tijera
		Definir usuario, PC Como Entero
		Pc =Azar(3)+1
		Escribir "escoja"
		Escribir "1 - Piedra"
		Escribir "2 - Tijeras"
		Escribir "3 - Papel"
		Leer usuario
		Borrar Pantalla
		si pc = usuario Entonces
			Escribir "Empate"
		SiNo
			si pc = 1 y usuario = 2 Entonces
				Escribir "La PC gana usted escogio tijera y la pc papel"
			SiNo
				si pc = 1 y usuario = 3 Entonces
					Escribir "Usted gana la PC escogio piedra y usted papel"
				SiNo
					si pc = 2 y usuario = 1 Entonces
						Escribir "Usted gana la PC escogio tijera y usted Piedra"
					SiNo
						si pc = 2 y usuario = 3 Entonces
							escribir "La PC gana usted escogio Papel y la pc tijeras"
						SiNo
							si pc = 3 y usuario = 1 Entonces
								escribir "La PC gana usted escogio Piedra y la PC Papel"
							SiNo
								Escribir "Usted gana la PC escogio Papel y usted Tijeras"
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
		
FinAlgoritmo
