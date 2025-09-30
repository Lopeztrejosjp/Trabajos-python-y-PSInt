#def nombre_de_la_funcion(parametro1, parametro2):
    #codigo de la funcion 

def saludar(nombre):
    mensaje = f"hola , {nombre}"
    print(mensaje)

saludar("Juan")

def suma(a, b):
    resultado = a + b
    return resultado

resultado = suma (5,5)
print(resultado)

def area_rectangulo (base, altura):
    area = base * altura
    return area 

base = int(input("ingrese el valor de la base "))
altura = int(input("ingrese la altura "))

area = area_rectangulo(base, altura)
print(area)

print(dir(__builtins__))
help(print)

print("hola","Mundo","todo","bien", sep= "*")