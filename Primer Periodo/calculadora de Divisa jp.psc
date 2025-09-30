Algoritmo Divisa 
	dolar = 506
	euro = 549 
	escribir "ingrese la cantidad de colones que desea covertir "
	leer cantidad 
	escribir "a que moneda desea convertir"
	escribir " 1-dolar "
	escribir " 2- euro "
	leer respuesta 
	Segun respuesta Hacer
		1:
			escribir " la conversion de colones a dolares es " cantidad/dolar "dolares"
		2:
			escribir " la coversion de colones a euros es  " cantidad/euro "euros" 
		
		
		De Otro Modo:
			escribir "usted escogio una opcion no valida" 
	Fin Segun

	
FinAlgoritmo
