print("ingrese su nombre")
nombre = input()
print("hola! ", nombre ,"Como andamos?")

num1= 40
num2 = 20
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(" La suma de " + str(num1) + " y " + str(num2) + " es " + str(suma))
print(" La resta de " + str(num1) + " y " + str(num2) + " es " + str(resta))
print(" La multiplicacion de " + str(num1) + " y " + str(num2) + " es " + str(multiplicacion))
print(" La division de " + str(num1) + " y " + str(num2) + " es " + str(division))

listaproductoss = ["arroz", "leche", "tomate", "Lechuga", "mayonesa"]
print(listaproductoss[2])
print(listaproductoss.append("caballo"))
print(listaproductoss)

numm1= int(input("Ingrese un numero entero"))
numm2 = int(input("ingrese un segundo numero"))
numm3 = int(input("ingrese un tercer numero"))
mayor = 0

if numm1 >= numm2 and numm1 >= numm3:
    mayor = numm1

if numm2 >= numm1 and numm2 >= numm3:
    mayor = numm2

if numm3 >= numm1 and numm3 >= numm3:
    mayor = numm3


print(f"el numero mayor es ", {mayor})


numeros_flotantes = [15.5, 23.7, 4.2, 8.1, 19.3]
suma_numeros = sum(numeros_flotantes)
cantidad_elementos = len(numeros_flotantes)
if cantidad_elementos > 0:
    promedio = suma_numeros / cantidad_elementos
else:
    promedio = 0
print(f"la lusta de numeros es  {numeros_flotantes}")
print(f"la suma de los numeros es {suma_numeros}")
print(f"la cantidad de elementos es {cantidad_elementos}")
print(f"el promedio es {promedio}")

lista_dupliicados = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = list(set(lista_dupliicados))
print ("la lista arreglada es", lista_sin_duplicados)

frase = input("por favor ingrese una frase ")
vocales = "aeiouáéíóú"
contador_vocales = 0
frase_min = frase.lower
for letra in frase_min:
    if letra in vocales:
        contador_vocales += 1

print(f"la frase ingresada es ", {frase})
print(f"el numero total de vocales es ", {contador_vocales})


#5
try:
    nump = int(input("por favor ingrese un numero entero "))
if nump % 2 == 0:
    print(f"el numero ", {nump} " es par")
else:
    print(f"el numero ", {nump} " es impar")

except ValueError:
print(f"el valor no es valido ")
