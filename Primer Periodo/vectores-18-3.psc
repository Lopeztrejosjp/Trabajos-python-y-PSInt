Algoritmo ejerciciosv
	dimension lista[10]
	
	Para x = 1 Hasta 10 Con Paso 1 Hacer
		Borrar Pantalla
		Escribir "ingrese un numero"
		leer num
		lista[x] = num 
		suma = suma + num 
	Fin Para
	
	Para x = 1 Hasta 10 Con Paso 1 Hacer
		Escribir lista[x] 
	Fin Para
	Escribir "el total de suma de los numeros es " suma 	
FinAlgoritmo
