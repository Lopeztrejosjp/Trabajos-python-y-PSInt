funcion nombre_de_cliente
	escribir "ingrese su nombre de cliente"
	leer nombre
FinFuncion
Algoritmo super_mercado 
	dimension lista_productos[10,2]
	para x=1 hasta 10 con paso 1 hacer 
		Escribir "lista de productos"
		Escribir "arroz 1000"
		escribir "aceite 2000"
		escribir "queso 3000"
		escribir "frijoles 4000"
		escribir "fresco 5000"
		
		escribir "ingrese el nombre del producto"
		leer producto
		escribir "ingrese el precio del producto"
		leer precio 
		
		total = total + precio 
		
		lista_productos[x,1] = articulo 
		lista_productos[x,2] = ConvertirATexto( precio ) 
		Esperar Tecla
		Borrar Pantalla
	FinPara
	si total > 100000 Entonces
		preciofinal = total - (total*0.10) 
		Escribir "a su compra se le aplico un descuento de 10% y el total es " preciofinal
	SiNo
		escribir "su compra es un total de " total
	FinSi
	

	
FinAlgoritmo
