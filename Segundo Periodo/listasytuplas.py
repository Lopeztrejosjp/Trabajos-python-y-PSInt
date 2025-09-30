# Definir una lista
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtener una porción desde el inicio hasta el índice 6 (sin incluir)
porcion1 = mi_lista[:6]
print(porcion1)  # Imprime [1, 2, 3, 4, 5, 6]

# Obtener una porción desde el índice 7 hasta el final
porcion2 = mi_lista[7:]
print(porcion2)  # Imprime [8, 9, 10]

# Obtener una porción desde el índice 2 hasta el índice 8 (sin incluir)
porcion3 = mi_lista[2:8]
print(porcion3)  # Imprime [3, 4, 5, 6, 7, 8]

# Utilizar índices negativos para contar desde el final
porcion4 = mi_lista[-5:-1]
print(porcion4)  # Imprime [6, 7, 8, 9]

# Obtener toda la lista (equivalente a lista[:])
copia_completa = mi_lista[:]
print(copia_completa)  # Imprime [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtener una porción con un paso (cada segundo elemento)
porcion_con_paso = mi_lista[::2]
print(porcion_con_paso)  # Imprime [1, 3, 5, 7, 9]
