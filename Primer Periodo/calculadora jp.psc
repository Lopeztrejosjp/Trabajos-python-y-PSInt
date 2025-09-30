Algoritmo Calculadora
	definir respuesta como entero 
	definir num1, num2 como real 
	
	escribir "que operacion quiere realizar? "
	escribir " 1 - sumar "
	escribir " 2 - restar "
	escribir " 3 - multiplicar "
	escribir " 4 - dividir "
	leer respuesta 
	
	escribir "ingrese el primer numero"
	leer num1 
	escribir "ingrese el segundo numero" 
	leer num2
	Segun respuesta Hacer
		1:
			escribir "el resultado de la suma es.. " num1 +num2
		2:
			escribir "el resultado de la resta es.. " num1 -num2 
		3:
			escribir "el resultado de la multiplicacion es.. " num1 *num2 
		4: 
			escribir "el resultado de la division es.. " num1 /num2 
		De Otro Modo:
				escribir "usted no escogio una operacion a realizar "
	Fin Segun
	
	
FinAlgoritmo
