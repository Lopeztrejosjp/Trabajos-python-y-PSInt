Algoritmo ejerciciosvysumas
	dimension lista[10]
	
	Para x = 1 Hasta 10 Con Paso 1 Hacer
		Borrar Pantalla
		Escribir "ingrese un numero"
		leer num
		lista[x] = num 
		suma = suma + num 
		si num mod 2 = 0 Entonces
			sumaPar = sumaPar + num
		SiNo
			sumaImpar =  sumaImpar + num 
		FinSi
	Fin Para
	Borrar Pantalla
	Para x = 1 Hasta 10 Con Paso 1 Hacer
		Escribir lista[x] 
	Fin Para
	Escribir "el total de suma es " suma
	escribir "el total de la suma de los numeros pares es " sumaParescribir 
	escribir "el total de suma de los numeros impares es " sumaImpar 
	FinSi
FinAlgoritmo
