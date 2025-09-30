nombre=input("ingrese su nombre ")
tarea= "cocinar una maruchan"
estado= "pendiente"
print(f"{nombre} revisando tarea {tarea}" )

if estado == "pendiente":
    print (f"{nombre}, siga cocinando")
else:
    print(f"ha terminado de cocinar {nombre}, ya puede comer ")