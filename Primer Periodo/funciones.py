def restar (a, b):
    return a - b 
def multiplicar (a, b): 
    return a * b 
def dividir (a, b):
    if b == 0: 
        return "error division por cero"
    return a/b  

def sumar(a, b):
    return a + b 

def suma():
    n1 = int(input("ingrese el primer numero"))
    n2 = int(input("ingrese el segundo numero "))
    print(n1 + n2)

n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))
resultado = sumar(n1, n2)
print(f"el resultado de la suma es: {resultado}")

