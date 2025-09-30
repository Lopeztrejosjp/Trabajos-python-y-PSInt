num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))  

numeros = [num1, num2, num3]
numeros.sort()

if num1 == num2 and num2 == num3:
    print("Los numeros son iguales")   

elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Hay numeros repetidos")
    print("menor", numeros[0])
    print("medio", numeros[1])
    print("mayor", numeros[2])
else:
    print("Los numeros son diferentes")
    print("menor", numeros[0])
    print("medio", numeros[1])
    print("mayor", numeros[2])

if num1 == num2 == num3:
    print("Los tres números son iguales:", num1)
else:
    if num1 <= num2 and num1 <= num3:
        menor = num1
        if num2 <= num3:
            medio = num2
            mayor = num3
        else:
            medio = num3
            mayor = num2
    elif num2 <= num1 and num2 <= num3:
        menor = num2
        if num1 <= num3:
            medio = num1
            mayor = num3
        else:
            medio = num3
            mayor = num1
    else:
        menor = num3
        if num1 <= num2:
            medio = num1
            mayor = num2
        else:
            medio = num2
            mayor = num1

    # Comprobación si hay números iguales
    if num1 == num2 or num1 == num3 or num2 == num3:
        print("Hay números iguales.")
    print("Menor:", menor)
    print("Medio:", medio)
    print("Mayor:", mayor)