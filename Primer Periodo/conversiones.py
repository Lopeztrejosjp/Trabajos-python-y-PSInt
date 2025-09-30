precio = str("99.99")
def convertir_a_float(precio_str):
    precio_float = float(precio_str)
    print(type(precio_str))
    print(type(precio_float))
    cantidad_str = "5"
    cantidad_int = int(cantidad_str)
    total = precio_float * cantidad_int 
    print(f"el total es: {total}")

convertir_a_float(precio)