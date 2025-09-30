funcion impares 
	escribir "ingrese hasta que numero quiere sumar los numeros impares"
	leer num
	suma = 0
	para x=1 hasta num con paso 2 hacer 
		suma = suma + x
	FinPara
	escribir "el total de la suma de los numeros impares es ", suma
FinFuncion

funcion pares 
	escribir "ingrese hasta que numero quiere sumar los numeros pares"
	leer num
	suma = 0
	para x=0 hasta num con paso 1 hacer 
		suma = suma + x
	FinPara
	escribir "el total de la suma de los numeros pares es ", suma
FinFuncion

funcion tablas 
	definir num, i como entero 
	escribir "ingrese un numero del cual quiera ver su tabla"
	leer num
	i=1
	Repetir
		escribir num, " x ",i, " = " ,num * i
		i=i+1
	Hasta Que i>10
FinFuncion

Algoritmo ejerciciosvysumas
	salir=Falso
	
	Repetir
		escribir "que desea hacer"
		escribir "1-ver la suma de numeros pares"
		escribir "2-ver la suma de los numeros impares"
		escribir "3-ver las tablas de multiplicar"
		escribir "4-salir"
		
		leer opc
		segun opc hacer
			1:pares
			2:impares
			3:tablas
			4:escribir "tenga un buen dia"
				salir=verdadero 
				
			De Otro Modo:
				escribir "no escogio una opcion valida"
		FinSegun
	Hasta Que salir=verdadero 
	
FinAlgoritmo

