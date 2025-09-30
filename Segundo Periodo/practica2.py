def bienvenida (nombre, idioma = "español" ):
    if idioma == "español":
        print(f"hola {nombre} bienvenido ")
    elif idioma == "ingles":
        print(f"hello {nombre} welcome ")
    else:
        print("idioma no reconocido")
bienvenida("Jp")
bienvenida("Calde", idioma = "ingles")
bienvenida("Joseth", idioma= "aleman")