lista_numeros = [1, 2, 3, 4, 5]
lista_strings = ['apple', 'banana', 'cherry']
lista_mixta = [1, 'dos', True, 4.5]

primer_elemento = lista_numeros[0] #enseña el primer eleento de esa tabla
segundo_elemento = lista_strings[1] #enseña el segundo elemento de la lista strings, porque el orden va de 0,1,2,3 
ultimo_elemento = lista_mixta[-1] #enseña el ultimo elemento de la lista mixta, porque el ultimo elemento se pone con el -1

long = len(lista_mixta)
print(long)

lista_numeros.append(6) #agrega el 6 al final

lista_strings.insert(1, "orange") #agrega un elemento entre apple y banana 

ultimo_elemento = lista_numeros.pop() #elimina el ultimo elemento 
lista_strings.remove("banana") #elimina un objeto en específico 

lista_numeros.sort() #ordena las listas

lista_mixta.reverse() #le da vuelta a las listas 

# Creación de una tupla
coordenadas = (3, 7)

# Acceso a elementos
x = coordenadas[0]  # x es igual a 3

# Longitud de la tupla
longitud = len(coordenadas)  # longitud es igual a 2

# Desempaquetado de tuplas
a, b = coordenadas  # a es igual a 3, b es igual a 7

# Concatenación de tuplas
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla_concatenada = tupla1 + tupla2  # tupla_concatenada es igual a (1, 2, 3, 'a', 'b', 'c')

# Creación de un objeto range
mi_rango = range(0, 10, 2)

# Iteración sobre el rango
for numero in mi_rango:
    print(numero)  # Imprime 0, 2, 4, 6, 8

# Convertir el rango en una lista
lista_mi_rango = list(mi_rango)  # lista_mi_rango es igual a [0, 2, 4, 6, 8]

# Verificar si un valor está en el rango
esta_en_rango = 3 in mi_rango  # devuelve False

frutas = ["manzana","banana","naranja","uva"]
print (frutas)
print(f"El elemento en la posición 0 es:  {frutas[0]}")
frutas.append("kiwi")
print (frutas)
frutas.insert(2, "pera")
print (frutas)
frutas.remove("kiwi")
print (frutas)
print(f"La lista final es  {frutas}") 